# route-optimizer
A route optimization system that integrates real-world map data with sustainability metrics to minimize distance, cost, and CO₂ emissions.

This project combines API-based routing with graph algorithms (Dijkstra) in a hybrid model, making it practically useful.

For single-destination trips, routes are fetched from an API and enriched with fuel cost and CO₂ emission analysis based on vehicle type.

For multi-destination logistics, the system builds a graph from API distances and applies Dijkstra’s algorithm (with scope for Genetic Algorithms in the future).

This ensures the solution is both practical (real-world API data) and algorithmically strong (graph optimization), while keeping sustainability at the core.

Progress:

-Added user input for start location + multiple destinations
-Integrated OpenRouteService API to fetch distances instead of hardcoding
-Implemented a flexible [get_coords()] function that accepts both:
  -addresses(e.g., "Delhi", "Connaught Place, Delhi")
  -coordinates (latitude, longitude)
-Displayed pairwise distances between all locations (start to provided multiple destination)
