import joblib

model = joblib.load(
    "models/xgboost_model.pkl"
)


def score_route(features):

    prediction = model.predict(
        [features]
    )[0]

    return float(prediction)