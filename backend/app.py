from fastapi import FastAPI
from services.route_service import get_route
from services.real_route_service import get_route as get_real_route

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Green Logistics Optimiser"}


@app.get("/route")
def route(source: str, destination: str):
    try:
        return get_route(source, destination)
    except Exception as e:
        return {"error": str(e), "type": type(e).__name__}


@app.get("/real-route")
def real_route(
    source_lat: float,
    source_lon: float,
    dest_lat: float,
    dest_lon: float
):
    return get_real_route(
        source_lat,
        source_lon,
        dest_lat,
        dest_lon
    )


@app.get("/intelligent-route")
def intelligent_route(
    source_lat: float,
    source_lon: float,
    dest_lat: float,
    dest_lon: float
):
    """
    IMPORTANT:
    This endpoint MUST call your intelligent router service.
    """
    from services.real_route_service import get_route as intelligent_get_route

    return intelligent_get_route(
        source_lat,
        source_lon,
        dest_lat,
        dest_lon
    )