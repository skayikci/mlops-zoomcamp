from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

@custom
def train_linear_model(df):
    df['PULocationID'] = df['PULocationID'].astype(str)
    df['DOLocationID'] = df['DOLocationID'].astype(str)

    # Prepare input features
    categorical = ['PULocationID', 'DOLocationID']
    dicts = df[categorical].to_dict(orient='records')

    # Fit DictVectorizer
    dv = DictVectorizer()
    X = dv.fit_transform(dicts)

    # Target variable
    y = df['duration'].values

    # Train Linear Regression
    model = LinearRegression()
    model.fit(X, y)

    print(f"Intercept: {model.intercept_:.2f}")
    print(f"Vectorizer: {dv}")
    print(f"Model: {model}")

    return dv, model
