from algorithms.real_graph import get_graph
from services.location_service import get_nearest_node
from services.candidate_routes import get_candidate_routes

print("Loading graph...")
graph = get_graph()

print("Finding source...")
source = get_nearest_node(
    28.6139,
    77.2090
)

print("Finding destination...")
destination = get_nearest_node(
    28.7041,
    77.1025
)

print("Generating routes...")
routes = get_candidate_routes(
    graph,
    source,
    destination
)

print("Candidate routes:", len(routes))

for i, route in enumerate(routes, start=1):
    print(
        f"Route {i}: {len(route)} nodes"
    )