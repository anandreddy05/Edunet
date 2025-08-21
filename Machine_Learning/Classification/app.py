import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("LogisticRegressionModel.pkl")

# Streamlit app
st.set_page_config(page_title="🌱 Sustainability Predictor", layout="centered")
st.title("🌍 Green Tech Sustainability Prediction")

st.markdown("Enter the feature values below to predict **Sustainability**")

# User inputs
carbon_emissions = st.number_input("Carbon Emissions", min_value=0.0, step=0.1)
energy_output = st.number_input("Energy Output", min_value=0.0, step=0.1)
renewability_index = st.number_input("Renewability Index (0–1)", min_value=0.0, max_value=1.0, step=0.01)
cost_efficiency = st.number_input("Cost Efficiency", min_value=0.0, step=0.1)

# Create dataframe for prediction
input_data = pd.DataFrame({
    "carbon_emissions": [carbon_emissions],
    "energy_output": [energy_output],
    "renewability_index": [renewability_index],
    "cost_efficiency": [cost_efficiency]
})

# Prediction button
if st.button("Predict Sustainability"):
    prediction = model.predict(input_data)[0]
    st.success(f"🌱 Predicted Sustainability Score: **{prediction:.2f}**")
