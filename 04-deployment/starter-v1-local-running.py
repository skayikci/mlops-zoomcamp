#!/usr/bin/env python
# coding: utf-8

import argparse
import pickle
import pandas as pd
import numpy as np
import os

# --- CLI args ---
parser = argparse.ArgumentParser()
parser.add_argument('--year', type=int, required=True)
parser.add_argument('--month', type=int, required=True)
args = parser.parse_args()

year = args.year
month = args.month

# --- Load model ---
with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

categorical = ['PULocationID', 'DOLocationID']

# --- Read + preprocess data ---
def read_data(filename):
    df = pd.read_parquet(filename)
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    return df

input_file = f'../data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
df = read_data(input_file)

# --- Predict ---
df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype(str)
dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)

# --- Save results ---
df_result = pd.DataFrame()
df_result['ride_id'] = df['ride_id']
df_result['prediction'] = y_pred

output_file = f'output/predictions_{year:04d}_{month:02d}.parquet'
os.makedirs('output', exist_ok=True)
df_result.to_parquet(output_file, engine='pyarrow', index=False)

# --- Report mean prediction ---
mean_pred = df_result['prediction'].mean()
print(f"Mean predicted duration: {mean_pred:.2f}")
