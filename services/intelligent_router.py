from services.route_ranker import score_route
from services.candidate_routes import get_candidate_routes
from services.feature_extractor import route_features


def choose_best_route(
    graph,
    source,
    destination
):

    routes = get_candidate_routes(
        graph,
        source,
        destination
    )

    best_route = None
    best_score = float("inf")

    for route in routes:

        features = route_features(
            route
        )

        score = score_route(
            features
        )

        if score < best_score:

            best_score = score
            best_route = route

    return best_route, best_score