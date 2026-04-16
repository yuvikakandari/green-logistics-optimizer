import streamlit as st
import requests

st.title(
    "Green Logistics Optimiser"
)

distance = st.slider(
    "Distance",
    1,
    50
)

traffic = st.slider(
    "Traffic",
    1,
    10
)

if st.button(
    "Predict Travel Time"
):

    response = requests.get(
        "http://127.0.0.1:8000/predict",
        params={
            "distance": distance,
            "traffic": traffic
        }
    )

    result = response.json()

    st.success(
        f"Predicted Time: {result['predicted_time']} mins"
    )