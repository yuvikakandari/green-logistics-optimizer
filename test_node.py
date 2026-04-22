import osmnx as ox

graph = ox.graph_from_place(
    "New Delhi, India",
    network_type="drive"
)

node = ox.distance.nearest_nodes(
    graph,
    77.2090,
    28.6139
)

print(node)