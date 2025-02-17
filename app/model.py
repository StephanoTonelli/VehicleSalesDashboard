import pandas as pd
import numpy as np
import seaborn as sns
import pyspark as spark
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from scipy import stats


def best_brand(filtered_df):
    df_make_value = filtered_df.groupby(["make"])[['sellingprice']].agg(['mean','sum','std'])

    df_make_volume = filtered_df.groupby(["make"])[['vin']].agg(['count'])

    best_brand_value_id = df_make_value['sellingprice']['sum'].idxmax()
    best_brand_value = df_make_value['sellingprice']['sum'].max()

    best_brand_volume_id = df_make_volume['vin']['count'].idxmax()
    best_brand_volume = df_make_volume['vin']['count'].max()

    
    return best_brand_value_id, best_brand_value, best_brand_volume_id, best_brand_volume

def best_model(filtered_df):

    df_make_value = filtered_df.groupby(["make","model"])[['sellingprice']].agg(['mean','sum','std'])

    df_make_volume = filtered_df.groupby(["make","model"])[['vin']].agg(['count'])

    best_model_value_id = df_make_value['sellingprice']['sum'].idxmax()[0] + " " + df_make_value['sellingprice']['sum'].idxmax()[1]
    best_model_value = df_make_value['sellingprice']['sum'].max()

    best_model_volume_id = df_make_volume['vin']['count'].idxmax()[0] + " " + df_make_volume['vin']['count'].idxmax()[1]
    best_model_volume = df_make_volume['vin']['count'].max()

    return best_model_value_id, best_model_value, best_model_volume_id, best_model_volume

def best_brand_body_type(filtered_df):
    # group by body and make and get the sum of sellingprice
    df_body_make_value = filtered_df.groupby(["body","make"])[['sellingprice']].agg(['sum'])

    # get the id of the max selling price for each body type
    # apply(lambda x: x[1]) gets a element of a list or tuple in case of x[0] is the first element of the tuple
    max_sales_per_body1 = df_body_make_value['sellingprice']['sum'].groupby("body").idxmax().apply(lambda x: x[1])

    # get the max selling price for each body type
    max_sales_per_body2 = df_body_make_value['sellingprice']['sum'].groupby("body").max()

    max_sales_per_body = pd.merge(max_sales_per_body1, max_sales_per_body2, left_index=True, right_index=True)

    #change name of columns
    max_sales_per_body.rename(columns={'sum_x': 'Make','sum_y': 'Total_SellingPrice'}, inplace=True)
    
    return max_sales_per_body

def best_model_body_type(filtered_df):
    # group by body, make and model and get the sum of sellingprice
    df_body_model_value = filtered_df.groupby(["body","make","model"])[['sellingprice']].agg(['sum'])

    # get the id of the max selling price for each body type
    # apply(lambda x: x[1]) gets a element of a list or tuple in case of x[0] is the first element of the tuple
    max_sales_body_model1 = df_body_model_value['sellingprice']['sum'].groupby("body").idxmax().apply(lambda x: x[1]+'/'+x[2])

    # get the max selling price for each body type
    max_sales_body_model2 = df_body_model_value['sellingprice']['sum'].groupby("body").max()

    max_sales_body_model = pd.merge(max_sales_body_model1, max_sales_body_model2, left_index=True, right_index=True)

    #change name of columns
    max_sales_body_model.rename(columns={'sum_x': 'Model','sum_y': 'Total_SellingPrice'}, inplace=True)
    
    return max_sales_body_model

def best_seller(filtered_df):
    # group by body and make and get the sum of sellingprice
    df_seller_value1 = filtered_df.groupby("seller")[["sellingprice"]].sum().sort_values(by="sellingprice", ascending=False)
    return df_seller_value1

def best_model_trend(filtered_df):
    df_best_selling_model_value = filtered_df.groupby(["body","make","model","year"])[["year","sellingprice"]].agg(['mean',"sum"])
    # Flatten the MultiIndex columns
    df_best_selling_model_value.columns = ['_'.join(col).strip() for col in df_best_selling_model_value.columns]

    df_best_selling_model_value1 = filtered_df.groupby(["body","make","model"])[["sellingprice"]].sum()

    #.rename(columns={'sellingprice_x': 'Total Sales Model','sellingprice_y': 'Year Sales Model'}, inplace=True)
    #.sort_values(by=["Total Sales Model"],ascending=False)


    df_best_selling_model = df_best_selling_model_value.merge(df_best_selling_model_value1, on=["body","make","model"])

    df_best_selling_model = df_best_selling_model.drop(['year_sum', 'sellingprice_mean',], axis=1)

    df_best_selling_model.rename(columns={'year_mean': 'Year','sellingprice': 'Total Sales Model','sellingprice_sum': 'Year Sales Model'}, inplace=True)

    df_best_selling_model.sort_values(by=["Total Sales Model","Year"],ascending=[False ,False])

    return df_best_selling_model

def average_price_distribution(filtered_df):
    df1 = filtered_df

    # print(df['saledate'].head())  # Check raw values before conversion
    # print(df.dtypes)  # Check current data types
    # df1['saledate'] = df1['saledate'].astype('datetime64[ns, UTC]').dt.strftime("%Y-%m")

    # calculates the average of the "Selling Price" and "mmr" columns for each unique value in the "saledate" column
    df1 = df1.groupby('Year_month').agg({'sellingprice': 'mean', 'mmr': 'mean'}).reset_index()

    return df1

def price_distribution_brand_category (filtered_df):
    df2 = filtered_df

    # calculates the average of the "Selling Price" and "mmr" columns for each unique value in the "saledate" column
    df2 = df2.groupby(['make','body',]).agg({'sellingprice': 'mean'}).reset_index()

    df2 = df2.nlargest(25, 'sellingprice')
    return df2

def seasonal_prices (filtered_df):
    df3 = filtered_df

    # Extract only the date part (YYYY-MM-DD)
    # df3['Year_month'] = df3['saledate'].astype('datetime64[ns, UTC]').dt.strftime("%Y-%m")

    df3.sort_values(by=["saledate"],ascending=[True])

    df3 = df3.dropna(subset=['saledate'])


    df3 = df3.groupby(['Year_month',"model"]).agg({'sellingprice': 'mean'}).reset_index()

    df3_top5 = df3.nlargest(10, 'sellingprice')

    df3 = df3[df3["model"].isin(df3_top5["model"])]

    df3.sort_values(by=["Year_month"],ascending=[True])
    
    return df3

def seasonal_sales (filtered_df):
    df4 = filtered_df

    # Extract only the date part (YYYY-MM-DD)
    # df4['Year_month'] = df4['saledate'].astype('datetime64[ns, UTC]').dt.strftime("%Y-%m")

    df4.sort_values(by=["saledate"],ascending=[True])

    df4 = df4.dropna(subset=['saledate'])


    df4 = df4.groupby(['Year_month',"make"]).agg({'vin': 'count'}).reset_index()

    df4_top = df4.nlargest(15, 'vin')

    df4 = df4[df4["make"].isin(df4_top["make"])]

    df4.sort_values(by=["Year_month"],ascending=[True])

    return df4

def odometer_price_correlation (filtered_df):
    df5 = filtered_df
    df5 = df5.dropna(subset=['odometer', 'sellingprice'])

    # Drop NaN values and ensure positive odometer values (log is undefined for non-positive values)
    df5 = df5.dropna(subset=['odometer', 'sellingprice'])
    df5 = df5[df5['odometer'] > 0]  # Ensure positive values for log transformation

    # Apply logarithm transformation to odometer
    df5['log_odometer'] = np.log(df5['odometer'])

    # Perform linear regression: sellingprice = a + b * log(odometer)
    b, a, r_value, p_value, std_err = stats.linregress(df5['log_odometer'], df5['sellingprice'])

    # Define the logarithmic function
    def _log_func(x):
        return a + b * np.log(x)

    # Generate trendline values
    df5_x_vals = np.linspace(df5['odometer'].min(), df5['odometer'].max(), 100)
    df5_y_vals = _log_func(df5_x_vals)

    return df5, df5_x_vals, df5_y_vals

def color_price_correlation (filtered_df):
    df6 = filtered_df
    df6 = df6.dropna(subset=["sellingprice"])

    q1 = df6["sellingprice"].quantile(0.25)
    q3 = df6["sellingprice"].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    df6 = df6[(df6["sellingprice"] >= lower_bound) & (df6["sellingprice"] <= upper_bound)]

    # Calculate median selling price for each color and sort in descending order
    median_order6 = df6.groupby("color")["sellingprice"].median().sort_values(ascending=False).index

    return df6, median_order6

def transmission_price_correlation (filtered_df):
    df7 = filtered_df
    df7 = df7.dropna(subset=["sellingprice"])

    q1 = df7["sellingprice"].quantile(0.25)
    q3 = df7["sellingprice"].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    df7 = df7[(df7["sellingprice"] >= lower_bound) & (df7["sellingprice"] <= upper_bound)]

    median_order7 = df7.groupby("transmission")["sellingprice"].median().sort_values(ascending=False).index

    return df7, median_order7

def condition_price_correlation (filtered_df):

    df8 = filtered_df
    # Drop NaN values and ensure positive odometer values (log is undefined for non-positive values)
    df8 = df8.dropna(subset=['condition', 'sellingprice'])
    df8 = df8[df8['condition'] > 0]  # Ensure positive values for log transformation

    # Perform linear regression: sellingprice = a + b * condition
    df8_b, df8_a, df8_r_value, df8_p_value, df8_std_err = stats.linregress(df8['condition'], df8['sellingprice'])

    # Define the logarithmic function
    def func(x):
        return df8_a + df8_b * x

    # Generate trendline values
    df8_x_vals = np.linspace(df8['condition'].min(), df8['condition'].max(), 100)
    df8_y_vals = func(df8_x_vals)

    return df8, df8_x_vals, df8_y_vals , df8_a, df8_b, df8_r_value
