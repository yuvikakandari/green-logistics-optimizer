"""
config.py

Central configuration for the Route Optimization Platform.

Keeping configurable values here allows the project to support
multiple cities and environments without modifying the core code.
"""

from pathlib import Path

# --------------------------------------------------
# Project directories
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

DATA_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

# --------------------------------------------------
# Map configuration
# --------------------------------------------------

CITY_NAME = "New Delhi, India"
NETWORK_TYPE = "drive"

GRAPH_FILE = DATA_DIR / "city_graph.graphml"

# --------------------------------------------------
# Machine Learning
# --------------------------------------------------

MODEL_FILE = MODELS_DIR / "xgboost_route_model.pkl"

# --------------------------------------------------
# Traffic simulation
# --------------------------------------------------

MIN_TRAFFIC_FACTOR = 1.0
MAX_TRAFFIC_FACTOR = 2.0