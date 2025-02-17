import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## if you cant find the package you created run the following code
# import os
# os.chdir('D:/DocumentsSte/VSCode/Proj1Streamlit')

from app.data_handler import df
from app.model import condition_price_correlation

# ----------------------------------------------------------------------------
### Page Title
st.title("Kaggle vehicle data")

# ----------------------------------------------------------------------------
### Side Bar FILTERS

# User input for scenario testing
st.sidebar.header("Filters")

# Filter years
first_year_filtered = st.sidebar.slider("Years", 1990, 2025, 1990)
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
### Run Models


df8, df8_x_vals, df8_y_vals, df8_a, df8_b, df8_r_value = condition_price_correlation(filtered_df)


# ----------------------------------------------------------------------------
### Display Visuals

st.write("### Interactive Filtered Data")
st.dataframe(filtered_df)  # Interactive table with sorting/filtering


# -------------------------------------- #
## Condition_price_correlation

# Create scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=df8['condition'], y=df8['sellingprice'], palette="coolwarm", ax=ax)

# Plot logarithmic trend curve
plt.plot(df8_x_vals, df8_y_vals, color='red', label='Trendline')

# Display the logarithmic equation
equation_text = f"y = {df8_b:.2f} + {df8_a:.2f} * x"
plt.text(0.05, 0.95, equation_text, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

# Labels and legend
ax.set_title("Condition vs Selling Price with Logarithmic Trendline")
ax.set_xlabel("Condition")
ax.set_ylabel("Selling Price ($)")
plt.legend()
st.pyplot(fig)

# Convert DataFrame to CSV (Fix: Convert DataFrame to string)
df8_csv = df8.to_csv(index=False).encode('utf-8')  # Convert string to bytes

# Download button
st.download_button(
    label="Download Data as CSV",
    data=df8_csv,
    file_name="Condition_price_correlation.csv",
    mime="text/csv"
)

# # Print equation details
# print(f"Equation of the logarithmic curve: y = {df8_b:.2f} + {df8_a:.2f} * x")
# print(f"R-squared value: {df8_r_value**2:.4f}")  # Goodness of fit measure

# -------------------------------------- #

