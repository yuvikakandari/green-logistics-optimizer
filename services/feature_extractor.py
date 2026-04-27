def route_features(route):

    distance = len(route)

    traffic = (distance % 10) + 1

    congestion = traffic * 0.7

    return [
        distance,
        traffic,
        congestion
    ]