from algorithms.real_graph import get_graph
from services.location_service import get_nearest_node
from services.candidate_routes import get_candidate_routes

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