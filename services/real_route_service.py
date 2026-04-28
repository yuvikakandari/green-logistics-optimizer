from services.location_service import get_nearest_node
from services.intelligent_router import choose_best_route
from algorithms.real_graph import get_graph


def get_route(
    source_lat,
    source_lon,
    dest_lat,
    dest_lon
):

    graph = get_graph()

    source = get_nearest_node(source_lat, source_lon)
    destination = get_nearest_node(dest_lat, dest_lon)

    route, predicted_eta = choose_best_route(
        graph,
        source,
        destination
    )

    # ----------------------------
    # ADD THIS: convert node path → coordinates
    # ----------------------------
    coords = []

    for node in route:
        try:
            lat = graph.nodes[node]["y"]
            lon = graph.nodes[node]["x"]
            coords.append((lat, lon))
        except KeyError:
            # safety fallback (prevents crashes)
            continue

    return {
        "route": route,
        "coords": coords,
        "predicted_eta": round(predicted_eta, 2),
        "source_node": source,
        "destination_node": destination,
        "model": "xgboost_v1"
    }