import osmnx as ox

graph = ox.graph_from_place(
    "New Delhi, India",
    network_type="drive"
)

print("Nodes:", len(graph.nodes))
print("Edges:", len(graph.edges))