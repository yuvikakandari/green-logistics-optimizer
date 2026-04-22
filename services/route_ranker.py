import joblib

model = joblib.load(
    "models/xgboost_model.pkl"
)


def score_route(
    distance,
    traffic
):

    prediction = model.predict(
        [[distance, traffic]]
    )[0]

    return float(prediction)