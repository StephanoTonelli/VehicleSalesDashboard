import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app.model import run_fleet_forecast
from app.data_handler import fetch_fleet_data

# Load data from API
st.title("FIPE Table Brazil")
# fleet_data = fetch_fleet_data()

# Sidebar: User input for scenario testing
st.sidebar.header("Model Parameters")
ev_growth_rate = st.sidebar.slider("p1", 0, 50, 10)
fleet_size_factor = st.sidebar.slider("p2", -10, 50, 0)


