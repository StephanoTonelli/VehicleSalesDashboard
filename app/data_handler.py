import pandas as pd
import requests

from config.auth import auth


def get_API_data():
    """Establish a connection to API."""
    response = requests.get(url)  # Make the request

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Convert response to JSON
    else:
        print(f"Error: {response.status_code}")
    
    return data
