import pandas as pd

@custom
def main():
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet'
    df = pd.read_parquet(url)
    print(f"Loaded {len(df):,} records")  # formatted with comma
    return df
