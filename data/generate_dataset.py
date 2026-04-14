import pandas as pd
import numpy as np

np.random.seed(42)

rows = []

for _ in range(1000):

    distance = np.random.randint(1, 50)

    traffic = np.random.randint(1, 10)

    travel_time = (
        distance * 1.5
        + traffic * 3
        + np.random.normal(0, 2)
    )

    rows.append(
        [distance, traffic, travel_time]
    )

df = pd.DataFrame(
    rows,
    columns=[
        "distance",
        "traffic",
        "travel_time"
    ]
)

df.to_csv(
    "data/routes.csv",
    index=False
)

print(df.head())