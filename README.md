## Structure of the project

Proj1Streamlit/
│── app/                    # Main application
│   │── __init__.py         # Marks it as a Python package
│   │── model.py            # Model logic (fleet forecasting)
│   │── data_handler.py     # Data retrieval from API
│   │── utils.py            # Helper functions
│── notebooks/              # Jupyter notebooks for testing
│── config/                 # Configuration files
│   │── config.py           # API credentials (avoid hardcoding)
│── main.py                 # Streamlit UI logic - Entry point to run the app
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation

## Explanation of the project

### Data

The first data set i got was from an API that would give me specific information on vehicles models and prices in Brazil.
Upon calling that API multiple times trying to fill my dataset I've reached its limit of requests so I had to look for another source of data.
My initial requests are in a Notebook called "data_API.ipynb"


The main data set from kaggle came from the following link:
https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data/data


### Intended results


- Best selling brand  -> **Best_Brand**
- Best selling model in the brand  -> **Best_Model**
- best selling brand in body type  -> **Best_Brand_Body_Type**
- best selling model in body type  -> **Best_Model_Body_Type**
- Best seller  -> **Best_Seller**
- selling trend of the best model over the years  -> **Best_Model_Trend**

- average price of the model selected and distribution of the prices - with average of mmr -> **Average_Price_Distribution**
- distribution of prices by brand and by category -> **Price_Distribution_Brand_Category**

- seasonal prices for each model -> **Seasonal_Prices**
- seasonal number of sales per make -> **Seasonal_Sales**

- correlation of odometer and price -> **odometer_price_correlation**
- correlation of color and price -> **color_price_correlation**
- correlation of transmission and price - compare means -> **transmission_price_correlation**
- correlation of condition and price -> **condition_price_correlation**