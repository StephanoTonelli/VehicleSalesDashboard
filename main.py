import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from app.data_handler import df
from app.model import model




# Load data from API
st.title("FIPE Table Brazil")
# fleet_data = fetch_fleet_data()

# Sidebar: User input for scenario testing
st.sidebar.header("Model Parameters")
ev_growth_rate = st.sidebar.slider("p1", 0, 50, 10)
fleet_size_factor = st.sidebar.slider("p2", -10, 50, 0)


st.write("### Using st.dataframe() (Interactive Table)")
st.dataframe(df)  # Interactive table with sorting/filtering

st.write("### Using st.table() (Static Table)")
st.table(df)  # Static table without interactivity