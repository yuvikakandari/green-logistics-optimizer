import streamlit as st
import openrouteservice
from openrouteservice import convert

# Title
st.title("Real-Address Route Optimizer")

# Get API Key from environment or paste it directly here
API_KEY = "YOUR_API_KEY" # ← Replace this with your actual OpenRouteService API key

client = openrouteservice.Client(key=API_KEY)

# Input boxes for addresses
start_address = st.text_input("Enter Starting Address", "MG Road, Delhi")
end_address = st.text_input("Enter Destination Address", "Paldi, Ahmedabad")

# Button to get route
if st.button("Calculate Route"):
    try:
        # Geocode both addresses to get coordinates
        start_coords = client.pelias_search(text=start_address)["features"][0]["geometry"]["coordinates"]
        end_coords = client.pelias_search(text=end_address)["features"][0]["geometry"]["coordinates"]

        # Get route data
        route = client.directions(
            coordinates=[start_coords, end_coords],
            profile='driving-car',
            format='geojson'
        )

        # Extract distance and duration
        summary = route["features"][0]["properties"]["summary"]
        distance_km = summary["distance"] / 1000
        duration_min = summary["duration"] / 60

        # Display result
        st.success(f"Distance: {distance_km:.2f} km")
        st.info(f"Estimated Travel Time: {duration_min:.1f} minutes")

    except Exception as e:
        st.error("Something went wrong! Check your addresses or API key.")
        st.code(str(e))
