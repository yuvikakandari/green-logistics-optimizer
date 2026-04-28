import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "xgboost_model.pkl")

model = joblib.load(MODEL_PATH)
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