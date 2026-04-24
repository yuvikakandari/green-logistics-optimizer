import osmnx as ox
import networkx as nx


def get_candidate_routes(
    graph,
    source,
    destination,
    k=3
):

    graph = ox.convert.to_digraph(
        graph,
        weight="length"
    )

    routes = list(
        nx.shortest_simple_paths(
            graph,
            source,
            destination,
            weight="length"
        )
    )

    return routes[:k]