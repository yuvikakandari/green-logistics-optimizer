"""
streamlit_app.py

Interactive dashboard for the Route Optimization Platform.
"""

import requests
import streamlit as st

st.set_page_config(
    page_title="Route Optimization Platform",
    layout="wide"
)

st.title("🚗 Intelligent Route Optimization")

st.markdown(
    "Find the optimal route using machine learning and graph algorithms."
)

start_lat = st.number_input(
    "Start Latitude",
    value=28.6129
)

start_lon = st.number_input(
    "Start Longitude",
    value=77.2295
)

end_lat = st.number_input(
    "Destination Latitude",
    value=28.6315
)

end_lon = st.number_input(
    "Destination Longitude",
    value=77.2167
)

if st.button("Find Route"):

    response = requests.post(

        "http://127.0.0.1:8000/route",

        json={

            "start_lat": start_lat,
            "start_lon": start_lon,
            "end_lat": end_lat,
            "end_lon": end_lon

        }

    )

    result = response.json()

    st.success("Route Computed Successfully")

    st.metric(
        "Predicted Cost",
        f"{result['predicted_cost']:.2f}"
    )

    st.metric(
        "Nodes Traversed",
        result["path_length"]
    )

    st.write("First 20 Nodes")

    st.write(result["path"][:20])