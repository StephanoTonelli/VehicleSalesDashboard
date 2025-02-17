import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## if you cant find the package you created run the following code
# import os
# os.chdir('D:/DocumentsSte/VSCode/Proj1Streamlit')

from app.data_handler import df
from app.model import best_brand, best_model, best_brand_body_type, best_model_body_type, best_seller, best_model_trend, average_price_distribution
from app.model import price_distribution_brand_category, seasonal_prices, seasonal_sales, odometer_price_correlation
from app.model import color_price_correlation, transmission_price_correlation, condition_price_correlation


# ----------------------------------------------------------------------------
### Page Title
st.title("Kaggle vehicle data")

# ----------------------------------------------------------------------------
### Side Bar FILTERS

# User input for scenario testing
st.sidebar.header("Filters")

# Filter years
first_year_filtered = st.sidebar.slider("Years", df["year"].min(), df["year"].max(), df["year"].min())
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

best_brand_value_id, best_brand_value, best_brand_volume_id, best_brand_volume = best_brand(filtered_df)

best_model_value_id, best_model_value, best_model_volume_id, best_model_volume = best_model(filtered_df)

best_brand_body_type = best_brand_body_type(filtered_df)

best_model_body_type = best_model_body_type(filtered_df)

df_seller_value1 = best_seller(filtered_df)

df_best_selling_model = best_model_trend(filtered_df)

df_average_price_distribution = average_price_distribution(filtered_df)

df_price_distribution_brand_category = price_distribution_brand_category(filtered_df)

df_seasonal_prices = seasonal_prices(filtered_df)

df_seasonal_sales = seasonal_sales(filtered_df)

df_odometer_price_correlation, x_vals_odometer_price_correlation, y_vals_odometer_price_correlation, a_odometer_price_correlation, b_odometer_price_correlation = odometer_price_correlation(filtered_df)

df_color_price_correlation, median_order_color_price_correlation = color_price_correlation(filtered_df)

df_transmission_price_correlation, median_order_transmission_price_correlation = transmission_price_correlation(filtered_df)

df8, df8_x_vals, df8_y_vals, df8_a, df8_b, df8_r_value = condition_price_correlation(filtered_df)


# ----------------------------------------------------------------------------
### Display Visuals


st.write("### Interactive Filtered Data")
st.dataframe(filtered_df)  # Interactive table with sorting/filtering


# -------------------------------------- #
st.divider()  # Creates a visual line

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Best Selling Brand by Value", value=str(f"{best_brand_value_id}"))
    st.metric(label="Total Sold", value=f"${best_brand_value:,}")
    st.divider()  # Creates a visual line
    st.metric(label="Best Selling Model by Value", value=str(f"{best_model_value_id}"))
    st.metric(label="Total Sold", value=f"${best_model_value:,}")


with col2:
    st.metric(label="Best Selling Brand by Volume", value=str(f"{best_brand_volume_id}"))
    st.metric(label="Total Sold", value=f"{best_brand_volume:,}")
    st.divider()  # Creates a visual line
    st.metric(label="Best Selling Model by Volume", value=str(f"{best_model_volume_id}"))
    st.metric(label="Total Sold", value=f"{best_model_volume:,}")

st.divider()  # Creates a visual line
# -------------------------------------- #

col2, col3 = st.columns(2)
with col2:
    best_brand_body_type = best_brand_body_type.nlargest(15, 'Total_SellingPrice')
    fig3, ax = plt.subplots()
    ax.set_title("Best make by body type")
    sns.barplot(data=best_brand_body_type, x="body", y="Total_SellingPrice", hue="Make", palette="Blues", edgecolor="black")
    plt.xticks(rotation=90) # Rotate x-axis labels vertically
    st.pyplot(fig3)
    
    # Convert DataFrame to CSV (Fix: Convert DataFrame to string)
    best_brand_body_type_csv = best_brand_body_type.to_csv(index=False).encode('utf-8')  # Convert string to bytes
    # Download button
    st.download_button(
        label="Download Data as CSV",
        data=best_brand_body_type_csv,
        file_name="best_brand_body_type.csv",
        mime="text/csv"
    )

with col3:
    best_model_body_type = best_model_body_type.nlargest(15, 'Total_SellingPrice')
    fig3, ax = plt.subplots()
    ax.set_title("Best model by body type")
    sns.barplot(data=best_model_body_type, x="body", y="Total_SellingPrice", hue="Model", palette="Blues", edgecolor="black")
    plt.xticks(rotation=90) # Rotate x-axis labels vertically
    st.pyplot(fig3)
        
    # Convert DataFrame to CSV (Fix: Convert DataFrame to string)
    best_model_body_type_csv = best_model_body_type.to_csv(index=False).encode('utf-8')  # Convert string to bytes
    # Download button
    st.download_button(
        label="Download Data as CSV",
        data=best_model_body_type_csv,
        file_name="best_model_body_type.csv",
        mime="text/csv"
    )

st.divider()  # Creates a visual line
# -------------------------------------- #

fig7, ax = plt.subplots()
ax.set_title("Average Price Distribution")
sns.lineplot(data=df_average_price_distribution, x="Year_month", y="sellingprice", marker="o", color="b", ax=ax)
sns.lineplot(data=df_average_price_distribution, x="Year_month", y="mmr", marker="o", color="r", ax=ax)
plt.xticks(rotation=90) # Rotate x-axis labels vertically
st.pyplot(fig7)

# Convert DataFrame to CSV (Fix: Convert DataFrame to string)
df_average_price_distribution_csv = df_average_price_distribution.to_csv(index=False).encode('utf-8')  # Convert string to bytes
# Download button
st.download_button(
    label="Download Data as CSV",
    data=df_average_price_distribution_csv,
    file_name="average_price_distribution.csv",
    mime="text/csv"
)


st.divider()  # Creates a visual line
# -------------------------------------- #

# df_odometer_price_correlation, x_vals_odometer_price_correlation, y_vals_odometer_price_correlation, a_odometer_price_correlation, b_odometer_price_correlation
# Create scatter plot
fig11, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=df_odometer_price_correlation['odometer'], y=df_odometer_price_correlation['sellingprice'], palette="coolwarm", ax=ax)

# Plot logarithmic trend curve
plt.plot(x_vals_odometer_price_correlation, y_vals_odometer_price_correlation, color='red', label='Logarithmic Trendline')

# Display the logarithmic equation
equation_text = f"y = {b_odometer_price_correlation:.2f} + {a_odometer_price_correlation:.2f} * ln(x)"
plt.text(0.05, 0.95, equation_text, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

# Labels and legend
ax.set_title("Odometer vs Selling Price with Logarithmic Trendline")
ax.set_xlabel("Odometer (km)")
ax.set_ylabel("Selling Price ($)")
plt.legend()
plt.show()
st.pyplot(fig11)

# Convert DataFrame to CSV (Fix: Convert DataFrame to string)
df_odometer_price_correlation_csv = df_odometer_price_correlation.to_csv(index=False).encode('utf-8')  # Convert string to bytes
# Download button
st.download_button(
    label="Download Data as CSV",
    data=df_odometer_price_correlation_csv,
    file_name="odometer_price_correlation.csv",
    mime="text/csv"
)


st.divider()  # Creates a visual line
# -------------------------------------- #



# -------------------------------------- #


# -------------------------------------- #
## Condition_price_correlation

# Create scatter plot
fig14, ax = plt.subplots(figsize=(10, 6))
sns.set_style("dark") # Options: "white", "dark", "whitegrid", "darkgrid", "ticks"
sns.scatterplot(x=df8['condition'], y=df8['sellingprice'], palette="coolwarm", ax=ax)

# Plot logarithmic trend curve
plt.plot(df8_x_vals, df8_y_vals, color='red', label='Trendline')

# Display the logarithmic equation
equation_text = f"y = {df8_b:.2f} + {df8_a:.2f} * x"
plt.text(0.05, 0.95, equation_text, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

# Display R-squared value
equation_text = f"R-squared value: {df8_r_value**2:.4f}"
plt.text(0.05, 0.88, equation_text, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

# Labels and legend
ax.set_title("Condition vs Selling Price with Logarithmic Trendline")
ax.set_xlabel("Condition")
ax.set_ylabel("Selling Price ($)")
plt.legend()
st.pyplot(fig14)

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

