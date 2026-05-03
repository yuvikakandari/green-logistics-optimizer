"""
streamlit_app.py

Interactive dashboard for the Route Optimization Platform.
"""

import folium
import requests
import streamlit as st
from streamlit_folium import st_folium


API_URL = "http://127.0.0.1:8000/route"


st.set_page_config(
    page_title="Route Optimization Platform",
    layout="wide",
)

st.title("🚗 Intelligent Route Optimization")
st.markdown(
    "Find the optimal route using machine learning and graph algorithms."
)

# Keeps the latest route visible even when Streamlit reruns,
# such as after zooming or panning the map.
if "route_result" not in st.session_state:
    st.session_state.route_result = None


start_lat = st.number_input(
    "Start Latitude",
    value=28.6129,
    format="%.6f",
)

start_lon = st.number_input(
    "Start Longitude",
    value=77.2295,
    format="%.6f",
)

end_lat = st.number_input(
    "Destination Latitude",
    value=28.6315,
    format="%.6f",
)

end_lon = st.number_input(
    "Destination Longitude",
    value=77.2167,
    format="%.6f",
)


if st.button("Find Route", type="primary"):
    request_payload = {
        "start_lat": start_lat,
        "start_lon": start_lon,
        "end_lat": end_lat,
        "end_lon": end_lon,
    }

    try:
        with st.spinner("Computing optimized route..."):
            response = requests.post(
                API_URL,
                json=request_payload,
                timeout=120,
            )

        response.raise_for_status()

        st.session_state.route_result = response.json()

    except requests.RequestException as error:
        st.session_state.route_result = None
        st.error(
            "Could not connect to the routing API. "
            "Make sure FastAPI is running on port 8000."
        )
        st.exception(error)


# This stays outside the button block so it persists after map interaction.
if st.session_state.route_result is not None:
    result = st.session_state.route_result
    coordinates = result.get("coordinates", [])

    if len(coordinates) < 2:
        st.error("The API returned an invalid route with too few coordinates.")
    else:
        st.success("Route Computed Successfully")

        metric_col_1, metric_col_2 = st.columns(2)

        metric_col_1.metric(
            "Predicted Cost",
            f"{result['predicted_cost']:.2f}",
        )

        metric_col_2.metric(
            "Nodes Traversed",
            result["path_length"],
        )

        route = [
            [point["lat"], point["lon"]]
            for point in coordinates
        ]

        route_map = folium.Map(
            location=route[0],
            zoom_start=14,
        )

        folium.Marker(
            route[0],
            tooltip="Start",
            icon=folium.Icon(color="green"),
        ).add_to(route_map)

        folium.Marker(
            route[-1],
            tooltip="Destination",
            icon=folium.Icon(color="red"),
        ).add_to(route_map)

        folium.PolyLine(
            route,
            weight=5,
            color="blue",
        ).add_to(route_map)

        st_folium(
            route_map,
            width=None,
            height=600,
            key="route_map",
        )