from algorithms.graph_loader import get_graph
from algorithms.dijkstra import dijkstra

graph = get_graph()

nodes = list(graph.nodes)

start_node = nodes[0]
end_node = nodes[100]

distance, path = dijkstra(
    graph,
    start_node,
    end_node
)

print("Distance:", distance)
print("Path length:", len(path))