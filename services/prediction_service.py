import joblib


model = joblib.load(
    "models/xgboost_model.pkl"
)


def predict_time(
    distance,
    traffic
):

    prediction = model.predict(
        [[distance, traffic]]
    )[0]

    return round(
        float(prediction),
        2
    )