import networkx as nx

from services.traffic_simulator import get_live_traffic


def build_graph():

    graph = nx.Graph()

    traffic = get_live_traffic()

    graph.add_edge(
        "Warehouse",
        "Hub_A",
        distance=5,
        traffic=traffic[("Warehouse", "Hub_A")]
    )

    graph.add_edge(
        "Warehouse",
        "Hub_C",
        distance=8,
        traffic=traffic[("Warehouse", "Hub_C")]
    )

    graph.add_edge(
        "Hub_A",
        "Hub_B",
        distance=4,
        traffic=traffic[("Hub_A", "Hub_B")]
    )

    graph.add_edge(
        "Hub_C",
        "Hub_B",
        distance=3,
        traffic=traffic[("Hub_C", "Hub_B")]
    )

    graph.add_edge(
        "Hub_B",
        "Customer",
        distance=5,
        traffic=traffic[("Hub_B", "Customer")]
    )

    for u, v, data in graph.edges(data=True):

        data["weight"] = (
            data["distance"]
            + data["traffic"]
        )

    return graph