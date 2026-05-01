"""
intelligent_router.py

Integrates machine learning with graph routing.
"""

from algorithms.graph_loader import get_graph
from algorithms.dijkstra import dijkstra

from ml.feature_engineering import extract_edge_features
from ml.predictor import RouteCostPredictor


class IntelligentRouter:

    def __init__(self):

        self.graph = get_graph()

        self.predictor = RouteCostPredictor()

    def assign_predicted_costs(self):
        """
        Predict cost for every edge in the graph.
        """

        print("Predicting edge costs...")

        for _, _, _, edge in self.graph.edges(keys=True, data=True):

            features = extract_edge_features(edge)

            predicted_cost = self.predictor.predict(features)

            edge["predicted_cost"] = predicted_cost

    def shortest_route(
        self,
        start_node,
        end_node
    ):
        """
        Compute shortest route using predicted costs.
        """

        return dijkstra(
            self.graph,
            start_node,
            end_node,
            weight="predicted_cost"
        )