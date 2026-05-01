"""
train_model.py

Train an XGBoost regression model to predict
route travel cost from engineered features.
"""

import joblib
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from config import MODEL_FILE


def train():
    """
    Train the XGBoost model.
    """

    dataset = pd.read_csv("data/routes.csv")

    X = dataset[
        [
            "distance",
            "speed_limit",
            "traffic_factor"
        ]
    ]

    y = dataset["travel_time"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = XGBRegressor(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    print(f"Mean Absolute Error: {mae:.2f}")

    joblib.dump(model, MODEL_FILE)

    print(f"Model saved to {MODEL_FILE}")


if __name__ == "__main__":
    train()