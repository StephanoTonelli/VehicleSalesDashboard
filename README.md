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

Dataset Description:
The "Vehicle Sales and Market Trends Dataset" provides a comprehensive collection of information pertaining to the sales transactions of various vehicles. This dataset encompasses details such as the year, make, model, trim, body type, transmission type, VIN (Vehicle Identification Number), state of registration, condition rating, odometer reading, exterior and interior colors, seller information, Manheim Market Report (MMR) values, selling prices, and sale dates.

Key Features:
Vehicle Details: Includes specific information about each vehicle, such as its make, model, trim, and manufacturing year.

Transaction Information: Provides insights into the sales transactions, including selling prices and sale dates.

Market Trends: MMR values offer an estimate of the market value of each vehicle, allowing for analysis of market trends and fluctuations.

Condition and Mileage: Contains data on the condition of the vehicles as well as their odometer readings, enabling analysis of how these factors influence selling prices.

Potential Use Cases:

Market Analysis: Researchers and analysts can utilize this dataset to study trends in the automotive market, including pricing fluctuations based on factors such as vehicle condition and mileage.

Predictive Modeling: Data scientists can employ this dataset to develop predictive models for estimating vehicle prices based on various attributes.

Business Insights: Automotive industry professionals, dealerships, and financial institutions can derive insights into consumer preferences, market demand, and pricing strategies.

Format: The dataset is typically presented in tabular format (e.g., CSV) with rows representing individual vehicle sales transactions and columns representing different attributes associated with each transaction.

Data Integrity: Efforts have been made to ensure the accuracy and reliability of the data; however, users are encouraged to perform their own validation and verification processes.

Update Frequency: The dataset may be periodically updated to include new sales transactions and market data, providing fresh insights into ongoing trends in the automotive industry.



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