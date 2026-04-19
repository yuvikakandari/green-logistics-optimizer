from algorithms.real_dijkstra import shortest_path
from services.location_service import get_nearest_node


def get_route(
    source_lat,
    source_lon,
    dest_lat,
    dest_lon
):

    source = get_nearest_node(
        source_lat,
        source_lon
    )

    destination = get_nearest_node(
        dest_lat,
        dest_lon
    )

    route, distance = shortest_path(
        source,
        destination
    )

    return {
        "route": route,
        "distance_meters": round(distance, 2)
    }