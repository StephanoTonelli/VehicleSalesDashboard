import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
## if you cant find the package you created run the following code
import os
os.chdir('D:/DocumentsSte/VSCode/Proj1Streamlit')

from app.data_handler import df
from app.model import model

# ----------------------------------------------------------------------------
# Page Title
st.title("Kaggle vehicle data")

# ----------------------------------------------------------------------------
# Side Bar FILTERS

# User input for scenario testing
st.sidebar.header("Filters")

# Filter years
first_year_filtered = st.sidebar.slider("Years", 1990, 1990, 2025)
# Filter DataFrame if at least one category is selected
if first_year_filtered:
    filtered_df = df[(df['year'] >= first_year_filtered)]
else:
    filtered_df = df  # Show all data if no selection

# State filter
body_filtered = st.sidebar.multiselect("Select State", sorted(filtered_df['state'].unique()))
if body_filtered:
    filtered_df = filtered_df[filtered_df['state'].isin(body_filtered)]
else:
    filtered_df = filtered_df

# Make filter
make_filtered = st.sidebar.multiselect("Select Make", sorted(filtered_df['make'].unique()))
if make_filtered:
    filtered_df = filtered_df[filtered_df['make'].isin(make_filtered)]
else:
    filtered_df = filtered_df


# Model filter
model_filtered = st.sidebar.multiselect("Select Model", sorted(filtered_df['model'].unique()))
if model_filtered:
    filtered_df = filtered_df[filtered_df['model'].isin(model_filtered)]
else:
    filtered_df = filtered_df


# Body filter
body_filtered = st.sidebar.multiselect("Select Body", sorted(filtered_df['body'].unique()))
if body_filtered:
    filtered_df = filtered_df[filtered_df['body'].isin(body_filtered)]
else:
    filtered_df = filtered_df
    


# ----------------------------------------------------------------------------
# Run Model


# model_df, model_df1 = model(filtered_df)


# ----------------------------------------------------------------------------
# Display Visuals

st.write("### Interactive Table")
st.dataframe(filtered_df)  # Interactive table with sorting/filtering
