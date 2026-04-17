from algorithms.dijkstra import shortest_path
from services.prediction_service import predict_time


def get_route(source, destination):

    path, score = shortest_path(
        source,
        destination
    )

    distance = score

    traffic = 5

    eta = predict_time(
        distance,
        traffic
    )

    return {
        "path": path,
        "distance": distance,
        "eta": eta
    }