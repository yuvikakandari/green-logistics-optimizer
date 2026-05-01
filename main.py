from routing.intelligent_router import IntelligentRouter

router = IntelligentRouter()

router.assign_predicted_costs()

nodes = list(router.graph.nodes)

start = nodes[0]

end = nodes[500]

cost, path = router.shortest_route(
    start,
    end
)

print("\nOptimal Route")

print("-" * 40)

print("Predicted Cost :", cost)

print("Number of Nodes :", len(path))