import streamlit as st
import requests
import folium

from streamlit_folium import st_folium
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

if st.button("Find Optimal Route"):

    response = requests.get(
        "http://127.0.0.1:8000/route",
        params={
            "source": source,
            "destination": destination
        }
    )

    result = response.json()

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

    st_folium(
        m,
        width=900,
        height=500
    )