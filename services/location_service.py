import osmnx as ox

from algorithms.real_graph import get_graph


def get_nearest_node(lat, lon):

    graph = get_graph()

    return ox.distance.nearest_nodes(
        graph,
        lon,
        lat
    )