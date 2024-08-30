import streamlit as st
import requests
import json
from datetime import datetime

# Define the URL for the taxi fare prediction API
taxiFareApiUrl = 'https://taxifare.lewagon.ai/predict'

# Streamlit user interface
st.title("Taxi Fare Predictor")

# Inputs for pickup and dropoff locations
pickup_latitude = st.number_input("Pickup Latitude", value=40.71427)
pickup_longitude = st.number_input("Pickup Longitude", value=-74.00597)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.802)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.956)

# Input for passenger count
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=2)

# Input for pickup datetime
pickup_datetime = st.text_input("Pickup Datetime", value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Button to trigger prediction
if st.button('Predict Fare'):
    params = {
        "pickup_latitude":   pickup_latitude,
        "pickup_longitude":  pickup_longitude,
        "dropoff_latitude":  dropoff_latitude,
        "dropoff_longitude": dropoff_longitude,
        "passenger_count":   passenger_count,
        "pickup_datetime":   pickup_datetime
    }

    # Sending request to the API
    response = requests.get(taxiFareApiUrl, params=params)

    if response.status_code == 200:
        fare = response.json().get('fare')
        st.success(f'Predicted Fare: ${fare:.2f}')
    else:
        st.error(f"Error: {response.status_code}")
