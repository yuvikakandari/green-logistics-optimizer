"""
feature_engineering.py

Creates numerical features for every road segment.
These features will later be used to train the
XGBoost regression model.
"""

import random

# Estimated speed limits (km/h)
ROAD_SPEEDS = {
    "motorway": 90,
    "trunk": 80,
    "primary": 60,
    "secondary": 50,
    "tertiary": 40,
    "residential": 30,
    "service": 20,
}


def get_speed_limit(highway):
    """
    Returns estimated speed for a road type.
    """

    if isinstance(highway, list):
        highway = highway[0]

    return ROAD_SPEEDS.get(highway, 30)


def simulate_traffic():
    """
    Simulates traffic congestion.

    Returns
    -------
    float
        1.0 = no traffic
        2.0 = heavy traffic
    """

    return round(random.uniform(1.0, 2.0), 2)


def edge_features(edge):
    """
    Extract features from a road segment.

    Parameters
    ----------
    edge : dict

    Returns
    -------
    dict
    """

    length = edge.get("length", 0)

    highway = edge.get("highway", "residential")

    speed = get_speed_limit(highway)

    traffic = simulate_traffic()

    speed_mps = speed * 1000 / 3600

    travel_time = (length / speed_mps) * traffic

    return {
        "distance": length,
        "speed_limit": speed,
        "traffic_factor": traffic,
        "travel_time": travel_time,
    }