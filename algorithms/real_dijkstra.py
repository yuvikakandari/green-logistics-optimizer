import networkx as nx

from algorithms.real_graph import get_graph


def shortest_path(source_node, destination_node):

    graph = get_graph()

    route = nx.shortest_path(
        graph,
        source_node,
        destination_node,
        weight="length"
    )

    distance = nx.shortest_path_length(
        graph,
        source_node,
        destination_node,
        weight="length"
    )

    return route, distance