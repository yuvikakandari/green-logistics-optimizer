import sys
import streamlit as st
import os
import requests
import folium
from streamlit_folium import st_folium

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from config import CITY_NODES


st.set_page_config(
    page_title="Green Logistics Optimiser",
    layout="wide"
)

st.title("🚚 Green Logistics Optimiser")

source = st.selectbox(
    "Source",
    list(CITY_NODES.keys())
)

destination = st.selectbox(
    "Destination",
    list(CITY_NODES.keys()),
    index=len(CITY_NODES) - 1
)

if "route_result" not in st.session_state:
    st.session_state.route_result = None


if st.button("Find Optimal Route"):

    response = requests.get(
        "http://127.0.0.1:8000/route",
        params={
            "source": source,
            "destination": destination
        }
    )

    st.session_state.route_result = response.json()


if st.session_state.route_result:

    result = st.session_state.route_result

    st.subheader("Route Details")

    st.write(
        "Path:",
        " ➜ ".join(result["path"])
    )

    st.write(
        f"Route Score: {result['distance']}"
    )

    st.write(
        f"Predicted ETA: {result['eta']} mins"
    )

    route = result["path"]

    m = folium.Map(
        location=[28.6139, 77.2090],
        zoom_start=12
    )

    coordinates = []

    for node in route:

        lat, lon = CITY_NODES[node]

        coordinates.append([lat, lon])

        folium.Marker(
            [lat, lon],
            popup=node
        ).add_to(m)

    folium.PolyLine(
        coordinates,
        weight=5
    ).add_to(m)

    st.write("About to render map")

    

    st_folium(
        m,
         width=900,
         height=500
         returned_objects=[]
    )

    st.write("Map generated successfully")