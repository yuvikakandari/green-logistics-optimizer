from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load(
    "models/xgboost_model.pkl"
)


@app.get("/")
def home():

    return {
        "message":
        "Green Logistics Optimiser API"
    }


@app.get("/predict")
def predict(
    distance: float,
    traffic: float
):

    prediction = model.predict(
        [[distance, traffic]]
    )[0]

    return {
        "predicted_time":
        round(float(prediction), 2)
    }