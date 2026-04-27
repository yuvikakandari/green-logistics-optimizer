import numpy as np
import pandas as pd

from xgboost import XGBRegressor
import joblib

np.random.seed(42)

n = 5000

distance = np.random.randint(
    5,
    100,
    n
)

traffic = np.random.randint(
    1,
    10,
    n
)

congestion = traffic * np.random.uniform(
    0.5,
    1.5,
    n
)

eta = (
    distance * 1.2
    + traffic * 4
    + congestion * 3
)

df = pd.DataFrame({
    "distance": distance,
    "traffic": traffic,
    "congestion": congestion,
    "eta": eta
})

X = df[
    [
        "distance",
        "traffic",
        "congestion"
    ]
]

y = df["eta"]

model = XGBRegressor()

model.fit(
    X,
    y
)

joblib.dump(
    model,
    "models/xgboost_model.pkl"
)

print("Model saved")