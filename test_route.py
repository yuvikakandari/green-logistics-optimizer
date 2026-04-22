import osmnx as ox
import networkx as nx

graph = ox.graph_from_place(
    "New Delhi, India",
    network_type="drive"
)

source = ox.distance.nearest_nodes(
    graph,
    77.2090,
    28.6139
)

destination = ox.distance.nearest_nodes(
    graph,
    77.1025,
    28.7041
)

route = nx.shortest_path(
    graph,
    source,
    destination,
    weight="length"
)

print("Route length:", len(route))