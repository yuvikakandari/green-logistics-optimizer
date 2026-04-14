import networkx as nx


def build_graph():
    graph = nx.Graph()

    graph.add_edge("A", "B", weight=4)
    graph.add_edge("A", "D", weight=2)
    graph.add_edge("B", "C", weight=3)
    graph.add_edge("B", "E", weight=2)
    graph.add_edge("D", "E", weight=3)
    graph.add_edge("E", "C", weight=2)

    return graph


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


if __name__ == "__main__":
    path, distance = shortest_path("A", "C")

    print("Path:", path)
    print("Distance:", distance)