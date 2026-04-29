from services.traffic_simulator import get_traffic_factor


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
    if isinstance(highway, list):
        highway = highway[0]

    return ROAD_SPEEDS.get(highway, 30)


def extract_route_features(graph, route):
    """
    Extract features from a complete route.

    Parameters
    ----------
    graph : nx.MultiDiGraph
    route : list
        List of node IDs representing the route.

    Returns
    -------
    list
        [distance, avg_speed, avg_traffic, travel_time]
    """

    total_distance = 0
    total_time = 0
    traffic_values = []
    speed_values = []

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

        traffic = get_traffic_factor()

        speed_mps = speed * 1000 / 3600

        travel_time = (distance / speed_mps) * traffic

        total_distance += distance
        total_time += travel_time

        speed_values.append(speed)
        traffic_values.append(traffic)

    average_speed = sum(speed_values) / len(speed_values)
    average_traffic = sum(traffic_values) / len(traffic_values)

    return [
        total_distance,
        average_speed,
        average_traffic,
        total_time,
    ]