import osmnx as ox
import networkx as nx
from itertools import islice


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
    islice(
        nx.shortest_simple_paths(
            graph,
            source,
            destination,
            weight="length"
        ),
        k
    )
)

return routes