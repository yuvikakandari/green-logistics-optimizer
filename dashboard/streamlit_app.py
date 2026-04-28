import sys
import os
import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)

from config import CITY_NODES


st.set_page_config(
    page_title="Green Logistics Optimiser",
    layout="wide"
)

st.title("Green Logistics Optimiser")


# ----------------------------
# SESSION STATE (prevents UI reset)
# ----------------------------
if "route_result" not in st.session_state:
    st.session_state.route_result = None


# ----------------------------
# INPUTS (just UI, not used in API yet)
# ----------------------------
source = st.selectbox("Source", list(CITY_NODES.keys()))
destination = st.selectbox(
    "Destination",
    list(CITY_NODES.keys()),
    index=len(CITY_NODES) - 1
)


# ----------------------------
# CALL BACKEND
# ----------------------------
if st.button("Find Optimal Route"):

    response = requests.get(
        "http://127.0.0.1:8000/intelligent-route",
        params={
            "source_lat": CITY_NODES[source][0],
            "source_lon": CITY_NODES[source][1],
            "dest_lat": CITY_NODES[destination][0],
            "dest_lon": CITY_NODES[destination][1],
        }
    )

    if response.status_code != 200:
        st.error("Backend error")
        st.write(response.text)
        st.stop()

    try:
        result = response.json()
    except Exception as e:
        st.error(f"JSON parse error: {e}")
        st.write(response.text)
        st.stop()

    st.session_state.route_result = result


# ----------------------------
# DISPLAY RESULTS
# ----------------------------
if st.session_state.route_result:

    result = st.session_state.route_result

    st.subheader("Route Details")

    route = result.get("route", [])
    coords = result.get("coords", [])
    eta = result.get("predicted_eta", None)

    # Path display
    st.write("Path:")
    st.write(" ➜ ".join(str(x) for x in route))

    st.write(f"Predicted ETA: {eta} mins")


    # ----------------------------
    # MAP RENDERING
    # ----------------------------
    if coords:

        m = folium.Map(
            location=coords[0],
            zoom_start=13
        )

        folium.PolyLine(coords, weight=5, color="blue").add_to(m)

        for lat, lon in coords:
            folium.Marker([lat, lon]).add_to(m)

        st_folium(m, width=900, height=500)

    else:
        st.warning("No coordinates returned from backend")