from sklearn.feature_extraction import DictVectorizer

def main(df_train, df_val):
    def make_X(df, dv=None):
        dicts = df[["PU_DO", "trip_distance"]].to_dict(orient="records")
        if dv is None:
            dv = DictVectorizer()
            X = dv.fit_transform(dicts)
        else:
            X = dv.transform(dicts)
        return X, dv

    X_train, dv = make_X(df_train)
    X_val, _ = make_X(df_val, dv)
    y_train = df_train["duration"].values
    y_val = df_val["duration"].values

    return X_train, X_val, y_train, y_val, dv
