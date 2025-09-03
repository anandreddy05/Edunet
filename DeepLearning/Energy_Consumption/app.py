import streamlit as st
import numpy as np
import pickle
import os
import warnings

# Suppress TF & warning logs
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# warnings.filterwarnings("ignore")

# Load trained model
model = pickle.load(open("./model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Energy Consumption Predictor", page_icon="⚡", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 20px;
            border-radius: 15px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #4facfe, #00f2fe);
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 18px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #43e97b, #38f9d7);
        }
        .title {
            font-size: 36px;
            font-weight: 700;
            text-align: center;
            color: #2c3e50;
        }
        .prediction {
            font-size: 28px;
            font-weight: 700;
            color: #27ae60;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">⚡ Energy Consumption Prediction ⚡</h1>', unsafe_allow_html=True)

# Intro

# Placeholder image (you can replace with your own link)
st.image(
    "https://justenergy.com/wp-content/uploads/2023/08/energy-production-and-consumption-on-the-environment.jpeg",
    caption="Energy Usage Visualization",
    use_container_width=True
)
st.write("Enter the environmental conditions below to estimate the energy consumption.")

# Input Features
col1, col2 = st.columns(2)

with col1:
    temperature = st.slider("🌡 Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=0.5)
    humidity = st.slider("💧 Humidity (%)", min_value=0, max_value=100, value=50, step=1)

with col2:
    wind_speed = st.slider("🌬 Wind Speed (m/s)", min_value=0.0, max_value=30.0, value=5.0, step=0.5)
    solar_irradiance = st.slider("☀ Solar Irradiance (W/m²)", min_value=0, max_value=1200, value=500, step=10)
# Predict Button
if st.button("🔮 Predict Energy Consumption"):
    features = np.array([[temperature, humidity, wind_speed, solar_irradiance]])
    prediction = model.predict(features)
    prediction_value = float(prediction.flatten()[0])  # convert to scalar

    st.markdown(
        f'<p class="prediction">Predicted Energy Consumption: ⚡ {prediction_value:.2f} kWh</p>',
        unsafe_allow_html=True
    )
    

# Sidebar with extra info and images
st.sidebar.title("📊 Dashboard")
st.sidebar.write("This tool estimates **energy consumption** based on weather conditions.")
