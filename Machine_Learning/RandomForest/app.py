import streamlit as st
import joblib
import numpy as np

# Load model
with open("agricultural_sustainability_model.pkl", "rb") as f:
    model = joblib.load(f)

st.title("🌱 Sustainable Agriculture Prediction App")

st.write("Enter the values below to get predictions from the trained Random Forest model.")

# Input fields
soil_health = st.number_input("Soil Health", min_value=0.0, max_value=100.0, value=50.0)
crop_yield = st.number_input("Crop Yield", min_value=0.0, max_value=1000.0, value=200.0)
water_usage = st.number_input("Water Usage", min_value=0.0, max_value=1000.0, value=300.0)
carbon_footprint = st.number_input("Carbon Footprint", min_value=0.0, max_value=500.0, value=50.0)
fertilizer_use = st.number_input("Fertilizer Use", min_value=0.0, max_value=500.0, value=100.0)

# Convert inputs to numpy array
features = np.array([[soil_health, crop_yield, water_usage,
                      carbon_footprint, fertilizer_use]])

if st.button("Predict"):
    prediction = model.predict(features)
    st.success(f"🌾 Prediction: {prediction[0]}")
