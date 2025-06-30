import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add cities as nodes and distances as edges (in km)
G.add_edge("Delhi", "Jaipur", weight=280)
G.add_edge("Jaipur", "Udaipur", weight=400)
G.add_edge("Delhi", "Agra", weight=230)
G.add_edge("Agra", "Lucknow", weight=330)
G.add_edge("Delhi", "Lucknow", weight=550)
G.add_edge("Udaipur", "Ahmedabad", weight=260)
G.add_edge("Jaipur", "Ahmedabad", weight=660)
start = input("Enter starting city: ")
end = input("Enter destination city: ")

# Check if both cities are in the graph
if start in G.nodes and end in G.nodes:
    # Find shortest path using Dijkstra's algorithm
    path = nx.dijkstra_path(G, source=start, target=end, weight="weight")
    distance = nx.dijkstra_path_length(G, source=start, target=end, weight="weight")

    print(f"\nShortest route from {start} to {end}:")
    print(" → ".join(path))
    print(f"Total Distance: {distance} km")
else:
    print("One or both cities not found in the map.")

        