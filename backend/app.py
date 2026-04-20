from fastapi import FastAPI

from services.route_service import get_route

app = FastAPI()


@app.get("/")
def home():

    return {
        "message":
        "Green Logistics Optimiser"
    }


@app.get("/route")
def route(
    source: str,
    destination: str
):

    return get_route(
        source,
        destination
    )

@app.get("/real-route")
def real_route(
    source_lat: float,
    source_lon: float,
    dest_lat: float,
    dest_lon: float
):

    return get_route(
        source_lat,
        source_lon,
        dest_lat,
        dest_lon
    )