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