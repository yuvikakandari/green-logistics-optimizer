import networkx as nx

from algorithms.graph_builder import build_graph


def shortest_path(source, destination):

    graph = build_graph()

    path = nx.dijkstra_path(
        graph,
        source,
        destination,
        weight="weight"
    )

    distance = nx.dijkstra_path_length(
        graph,
        source,
        destination,
        weight="weight"
    )

    return path, distance