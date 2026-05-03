"""
app.py

FastAPI backend for the Route Optimization Platform.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from algorithms.graph_loader import get_graph
from routing.location_mapper import get_nearest_node
from routing.intelligent_router import IntelligentRouter

app = FastAPI(
    title="Route Optimization API",
    version="1.0.0"
)

graph = get_graph()

router = IntelligentRouter()

router.assign_predicted_costs()


class RouteRequest(BaseModel):

    start_lat: float
    start_lon: float

    end_lat: float
    end_lon: float


@app.get("/")
def health():

    return {
        "status": "running"
    }


@app.post("/route")
def optimize_route(request: RouteRequest):

    start_node = get_nearest_node(
        graph,
        request.start_lat,
        request.start_lon
    )

    end_node = get_nearest_node(
        graph,
        request.end_lat,
        request.end_lon
    )

    cost, path = router.shortest_route(
        start_node,
        end_node
    )
    coordinates = router.route_coordinates(path)
    return {

        "predicted_cost": cost,
        "path_length": len(path),
        "coordinates": coordinates
    }