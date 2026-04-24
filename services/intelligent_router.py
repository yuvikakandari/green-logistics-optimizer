from services.route_ranker import score_route
from services.candidate_routes import get_candidate_routes


def choose_best_route(
    graph,
    source,
    destination
):
    
    print("Using intelligent routing")

    routes = get_candidate_routes(
        graph,
        source,
        destination
    )

    best_route = None
    best_score = float("inf")

    for route in routes:

        distance = len(route)

        traffic = distance % 10 + 1

        score = score_route(
            distance,
            traffic
        )

        if score < best_score:

            best_score = score
            best_route = route

    print("Candidate routes:", len(routes))
    print("Best score:", best_score)

    return best_route, best_score