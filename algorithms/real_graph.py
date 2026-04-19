import osmnx as ox
import networkx as nx

CITY = "New Delhi, India"

graph = ox.graph_from_place(
    CITY,
    network_type="drive"
)


def get_graph():
    return graph