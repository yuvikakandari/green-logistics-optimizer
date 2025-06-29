import streamlit as st
import openrouteservice
from openrouteservice import convert

st.title("Real-Address Route Optimizer")
API_KEY = "5b3ce3597851110001cf6248729ae0da3c6342289d21452129e44d18" 

client = openrouteservice.Client(key=API_KEY)
start_address = st.text_input("Enter Starting Address", "MG Road, Delhi")
end_address = st.text_input("Enter Destination Address", "Paldi, Ahmedabad")
if st.button("Calculate Route"):
    try:
        start_coords = client.pelias_search(text=start_address)["features"][0]["geometry"]["coordinates"]
        end_coords = client.pelias_search(text=end_address)["features"][0]["geometry"]["coordinates"]

        route = client.directions(
            coordinates=[start_coords, end_coords],
            profile='driving-car',
            format='geojson'
        )
        summary = route["features"][0]["properties"]["summary"]
        distance_km = summary["distance"] / 1000
        duration_min = summary["duration"] / 60

        st.success(f"Distance: {distance_km:.2f} km")
        st.info(f"Estimated Travel Time: {duration_min:.1f} minutes")

    except Exception as e:
        st.error("Something went wrong! Check your addresses or API key.")
        st.code(str(e))
