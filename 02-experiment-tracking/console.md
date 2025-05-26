## Question : 1 
@skayikci ➜ /workspaces/mlops-zoomcamp-course (main) $ mlflow --version
mlflow, version 2.22.0
## Question : 2
(base) $ /U/s/D/o/m/0/output tree
.
├── dv.pkl
├── test.pkl
├── train.pkl
└── val.pkl

1 directory, 4 files

## Experiment run outputs:
(mlops-env) $ /U/s/D/o/m/02-experiment-tracking python hpo.py
2025/05/26 14:09:04 INFO mlflow.tracking.fluent: Experiment with name 'random-forest-hyperopt' does not exist. Creating a new experiment.
🏃 View run debonair-hound-188 at: http://127.0.0.1:5003/#/experiments/1/runs/d63e78f27f3b42a48cf63567e7772792

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run bedecked-shrike-742 at: http://127.0.0.1:5003/#/experiments/1/runs/5fbb62b1cd1d4f99b54b8d7c6f02a042

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run blushing-shark-548 at: http://127.0.0.1:5003/#/experiments/1/runs/ffeb6be4aa8c4b98b391c878a8700cb6

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run abrasive-foal-567 at: http://127.0.0.1:5003/#/experiments/1/runs/81e213b7fd3145a3a5b20ed0fc0aaa60

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run adorable-squid-441 at: http://127.0.0.1:5003/#/experiments/1/runs/b3d4f3ffb33a4af6b623aacf0c00794d

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run resilient-flea-327 at: http://127.0.0.1:5003/#/experiments/1/runs/016a902570554abea8a4366c7839a9c2

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run awesome-cow-323 at: http://127.0.0.1:5003/#/experiments/1/runs/5175c237659d4ae28ef15223b2b8a7a4

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run tasteful-crow-667 at: http://127.0.0.1:5003/#/experiments/1/runs/394a4f8970954c4bb2e8c4cf5d8a56b0

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run burly-skink-471 at: http://127.0.0.1:5003/#/experiments/1/runs/d871189dc65a4278b2ed2c2e0dc3b84f

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run debonair-bird-570 at: http://127.0.0.1:5003/#/experiments/1/runs/70836e754a5341f4823c3198ed3cfa35

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run debonair-conch-954 at: http://127.0.0.1:5003/#/experiments/1/runs/91c77de3411f453a8d5e87d1ac847953

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run bold-skink-7 at: http://127.0.0.1:5003/#/experiments/1/runs/a9a42557be0444ffa6d33e5793500da1

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run whimsical-owl-628 at: http://127.0.0.1:5003/#/experiments/1/runs/887ba3f73fbc48b991190adaf3c0f4ec

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run bedecked-fish-562 at: http://127.0.0.1:5003/#/experiments/1/runs/a6fdfb68753d42a9b9ce622c8856ab98

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

🏃 View run gifted-crane-210 at: http://127.0.0.1:5003/#/experiments/1/runs/a96abab4ba8c4830942758803f171f35

🧪 View experiment at: http://127.0.0.1:5003/#/experiments/1         

100%|█| 15/15 [00:29<00:00,  1.96s/trial, best loss: 5.33541958855692
(mlops-env) $ /U/s/D/o/m/02-experiment-tracking 


## Registration logs:
(mlops-env) $ /U/s/D/o/m/02-experiment-tracking python register_model.py --data_path ./output --top_n 5

2025/05/26 14:12:19 INFO mlflow.tracking.fluent: Experiment with name 'random-forest-best-models' does not exist. Creating a new experiment.
Retraining top models...
Retraining model for run: 91c77de3411f453a8d5e87d1ac847953
2025/05/26 14:12:36 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
🏃 View run inquisitive-shad-913 at: http://127.0.0.1:5003/#/experiments/2/runs/992fea4c5e2e4e0f8c587b3f30ca3a1e
🧪 View experiment at: http://127.0.0.1:5003/#/experiments/2
Retraining model for run: 016a902570554abea8a4366c7839a9c2
2025/05/26 14:12:50 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
🏃 View run bedecked-moth-33 at: http://127.0.0.1:5003/#/experiments/2/runs/e98aa3e285f242acbec8aa7c090f9fed
🧪 View experiment at: http://127.0.0.1:5003/#/experiments/2
Retraining model for run: a96abab4ba8c4830942758803f171f35
2025/05/26 14:13:01 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
🏃 View run carefree-worm-910 at: http://127.0.0.1:5003/#/experiments/2/runs/10339ca2976d47a7995a80281d22b11f
🧪 View experiment at: http://127.0.0.1:5003/#/experiments/2
Retraining model for run: 81e213b7fd3145a3a5b20ed0fc0aaa60
2025/05/26 14:13:12 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
🏃 View run gentle-fox-6 at: http://127.0.0.1:5003/#/experiments/2/runs/133b1883fb3b4cd496f60966faa1914e
🧪 View experiment at: http://127.0.0.1:5003/#/experiments/2
Retraining model for run: 70836e754a5341f4823c3198ed3cfa35
2025/05/26 14:13:23 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
🏃 View run fortunate-stork-777 at: http://127.0.0.1:5003/#/experiments/2/runs/7277e550cb834a608d99a20fe8c9c8ca
🧪 View experiment at: http://127.0.0.1:5003/#/experiments/2
Best model test RMSE: 5.567408012462019
Registering model from URI: runs:/992fea4c5e2e4e0f8c587b3f30ca3a1e/model
Successfully registered model 'rf-best-model'.
2025/05/26 14:13:23 INFO mlflow.store.model_registry.abstract_store: Waiting up to 300 seconds for model version to finish creation. Model name: rf-best-model, version 1
Created version '1' of model 'rf-best-model'.