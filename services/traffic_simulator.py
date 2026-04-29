import random

TRAFFIC_RANGES = {
    "motorway": (1.0, 1.2),
    "trunk": (1.0, 1.3),
    "primary": (1.1, 1.5),
    "secondary": (1.2, 1.6),
    "tertiary": (1.2, 1.7),
    "residential": (1.3, 2.0),
    "service": (1.1, 1.8),
}


def get_traffic_factor(highway_type):
    """
    Simulates traffic congestion for a road segment.

    Parameters
    ----------
    highway_type : str or list
        Road type from the OSM graph.

    Returns
    -------
    float
        Traffic multiplier:
            1.0 = free-flow traffic
            2.0 = heavy congestion
    """

    if isinstance(highway_type, list):
        highway_type = highway_type[0]

    low, high = TRAFFIC_RANGES.get(highway_type, (1.0, 2.0))

    return round(random.uniform(low, high), 2)