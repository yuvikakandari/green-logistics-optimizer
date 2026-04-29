"""
feature_extractor.py

Extracts machine learning features from a computed route.

These features will later be used to train an XGBoost model
to predict route cost.
"""

from services.traffic_simulator import get_traffic_factor

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
    Returns an estimated speed for a road type.
    """

    if isinstance(highway, list):
        highway = highway[0]

    return ROAD_SPEEDS.get(highway, 30)


def extract_route_features(graph, route):
    """
    Extracts features from a route.

    Parameters
    ----------
    graph : networkx.MultiDiGraph
        Road network graph.
    route : list
        List of node IDs returned by Dijkstra.

    Returns
    -------
    dict
        Dictionary containing route features.
    """

    total_distance = 0
    total_travel_time = 0
    traffic_values = []

    for i in range(len(route) - 1):

        u = route[i]
        v = route[i + 1]

        edge = graph.get_edge_data(u, v)

        if edge is None:
            continue

        edge = edge[0]

        distance = edge.get("length", 0)

        highway = edge.get("highway", "residential")

        speed = get_speed_limit(highway)

        traffic = get_traffic_factor(highway)

        speed_mps = speed * 1000 / 3600

        travel_time = (distance / speed_mps) * traffic

        total_distance += distance
        total_travel_time += travel_time

        traffic_values.append(traffic)

    average_traffic = (
        sum(traffic_values) / len(traffic_values)
        if traffic_values
        else 1.0
    )

    return {
        "distance": total_distance,
        "average_traffic": average_traffic,
        "travel_time": total_travel_time,
    }