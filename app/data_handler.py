
import pandas as pd


def get_API_data():
    """Establish a connection to API."""
    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    return conn
