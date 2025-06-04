import mlflow
import mlflow.sklearn
import pickle
from pathlib import Path

@custom
def register_model(dv, model):
    print(f"Vectorizer: {dv}")
    print(f"Model: {model}")

    mlflow.set_tracking_uri("http://mlflow:5054")
    mlflow.set_experiment("yellow-taxi-lr")

    with mlflow.start_run():
        # Save vectorizer
        Path("artifacts").mkdir(exist_ok=True)
        with open("artifacts/dv.pkl", "wb") as f_out:
            pickle.dump(dv, f_out)
        mlflow.log_artifact("artifacts/dv.pkl", artifact_path="preprocessor")

        # Log the sklearn model
        mlflow.sklearn.log_model(model, artifact_path="models_lr")

        print("Model and vectorizer registered with MLflow.")
