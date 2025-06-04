from pathlib import Path

import pickle
import mlflow


mlflow.set_tracking_uri("http://localhost:5054")
mlflow.set_experiment("nyc-taxi-experiment")

models_folder = Path('models')
models_folder.mkdir(exist_ok=True)

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    dv, lr = data 
    with mlflow.start_run():
        with open('dict_vectorizer.bin', 'wb') as f_out:
            pickle.dump(dv, f_out)
        mlflow.log_artifact('dict_vectorizer.bin')

        mlflow.sklearn.log_model(lr, 'model')

    print('OK')


