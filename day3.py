import streamlit as st
import networkx as nx

# Page title
st.title(" Route Optimizer Shortest Path Finder")

# Build the graph
G = nx.Graph()
G.add_edge("Delhi", "Jaipur", weight=280)
G.add_edge("Jaipur", "Udaipur", weight=400)
G.add_edge("Delhi", "Agra", weight=230)
G.add_edge("Agra", "Lucknow", weight=330)
G.add_edge("Delhi", "Lucknow", weight=550)
G.add_edge("Udaipur", "Ahmedabad", weight=260)
G.add_edge("Jaipur", "Ahmedabad", weight=660)

# Create dropdowns for user input
cities = list(G.nodes)
start = st.selectbox("Select Starting City", cities)
end = st.selectbox("Select Destination City", cities)

# Button to calculate route
if st.button("Find Shortest Route"):
    if start == end:
        st.warning("Start and destination cannot be the same.")
    else:
        path = nx.dijkstra_path(G, source=start, target=end, weight="weight")
        distance = nx.dijkstra_path_length(G, source=start, target=end, weight="weight")

        # Show result
        st.success(f"Shortest route from {start} to {end}:")
        st.markdown(" → ".join(path))
        st.info(f"Total Distance: {distance} km")
