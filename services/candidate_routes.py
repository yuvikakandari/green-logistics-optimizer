import networkx as nx


def get_candidate_routes(
    graph,
    source,
    destination,
    k=3
):

    routes = list(
        nx.shortest_simple_paths(
            graph,
            source,
            destination,
            weight="length"
        )
    )

    return routes[:k]