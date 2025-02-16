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

- Best selling brand  -> X 
- Best selling model in the brand  -> X 
- best selling brand in body type  -> X 
- best selling model in body type  -> X 
- Best seller  -> X 
- selling trend of the best model over the years  -> X 


- average price of the model selected and distribution of the prices - with average of mmr -> X 
- distribution of prices by brand and by category -> X 

- seasonal prices for each model -> X
- seasonal number of sales per make -> X

- correlation of odometer and price -> X
- correlation of color and price -> X
- correlation of transmission and price - compare means -> X
- correlation of condition and price -> X