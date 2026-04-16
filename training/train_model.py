import pandas as pd
import joblib

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("data/routes.csv")

X = df[
    [
        "distance",
        "traffic"
    ]
]

y = df["travel_time"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

print("MAE:", mae)

joblib.dump(
    model,
    "models/xgboost_model.pkl"
)