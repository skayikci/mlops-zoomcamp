import pandas as pd
import pickle

def main(year: int, month: int):
    def load_df(y, m):
        url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{y}-{m:02d}.parquet'
        df = pd.read_parquet(url)
        df['duration'] = df.lpep_dropoff_datetime - df.lpep_p
        df['duration'] = df.duration.dt.total_seconds() / 60
        df = df[(df.duration >= 1) & (df.duration <= 60)]
        df[['PULocationID', 'DOLocationID']] = df[['PULocationID', 'DOLocationID']].astype(str)
        df['PU_DO'] = df['PULocationID'] + '_' + df['DOLocationID']
        return df

    df_train = load_df(year, month)
    next_year = year if month < 12 else year + 1
    next_month = month + 1 if month < 12 else 1
    df_val = load_df(next_year, next_month)

    return df_train, df_val
