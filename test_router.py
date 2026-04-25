from algorithms.real_graph import get_graph
from services.location_service import get_nearest_node
from services.intelligent_router import choose_best_route

graph = get_graph()

source = get_nearest_node(
    28.6139,
    77.2090
)

destination = get_nearest_node(
    28.7041,
    77.1025
)

route, score = choose_best_route(
    graph,
    source,
    destination
)

print("Best route length:", len(route))
print("Predicted score:", score)