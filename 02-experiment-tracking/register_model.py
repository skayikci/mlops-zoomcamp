import os
import pickle
import click
import mlflow

from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

# Constants
HPO_EXPERIMENT_NAME = "random-forest-hyperopt"
EXPERIMENT_NAME = "random-forest-best-models"
RF_PARAMS = ['max_depth', 'n_estimators', 'min_samples_split', 'min_samples_leaf', 'random_state']

# MLflow setup
mlflow.set_tracking_uri("http://127.0.0.1:5003")
mlflow.set_experiment(EXPERIMENT_NAME)
mlflow.sklearn.autolog()

# Helper to load data
def load_pickle(filename):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)

# Train model and log metrics + model
def train_and_log_model(data_path, params):
    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))
    X_test, y_test = load_pickle(os.path.join(data_path, "test.pkl"))

    for param in RF_PARAMS:
        params[param] = int(params[param])

    rf = RandomForestRegressor(**params)
    rf.fit(X_train, y_train)

    val_preds = rf.predict(X_val)
    test_preds = rf.predict(X_test)

    val_rmse = root_mean_squared_error(y_val, val_preds)
    test_rmse = root_mean_squared_error(y_test, test_preds)

    mlflow.log_metric("val_rmse", val_rmse)
    mlflow.log_metric("test_rmse", test_rmse)

    mlflow.sklearn.log_model(rf, artifact_path="model")

# Main CLI
@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
@click.option(
    "--top_n",
    default=5,
    type=int,
    help="Number of top models that need to be evaluated to decide which one to promote"
)
def run_register_model(data_path: str, top_n: int):
    client = MlflowClient()
    print("Retraining top models...")


    # Get top_n best HPO runs based on validation RMSE
    hpo_experiment = client.get_experiment_by_name(HPO_EXPERIMENT_NAME)
    hpo_runs = client.search_runs(
        experiment_ids=hpo_experiment.experiment_id,
        run_view_type=ViewType.ACTIVE_ONLY,
        max_results=top_n,
        order_by=["metrics.rmse ASC"]
    )

    new_run_ids = []

    # Retrain and log under best-models experiment
    for hpo_run in hpo_runs:
        print(f"Retraining model for run: {hpo_run.info.run_id}")
        with mlflow.start_run():
            params = {k: v for k, v in hpo_run.data.params.items()}
            run_id = mlflow.active_run().info.run_id
            new_run_ids.append(run_id)
            train_and_log_model(data_path=data_path, params=params)

    # Find run with lowest test RMSE
    best_run_id = None
    best_rmse = float("inf")

    for run_id in new_run_ids:
        run = client.get_run(run_id)
        test_rmse = run.data.metrics.get("test_rmse")
        if test_rmse is not None and test_rmse < best_rmse:
            best_rmse = test_rmse
            best_run_id = run_id

    if best_run_id is None:
        raise RuntimeError("No valid run found with test_rmse")

    print(f"Best model test RMSE: {best_rmse}")
    model_uri = f"runs:/{best_run_id}/model"

    # Register model
    print(f"Registering model from URI: {model_uri}")
    mlflow.register_model(model_uri=model_uri, name="rf-best-model")

if __name__ == '__main__':
    run_register_model()
