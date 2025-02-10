import pandas as pd


def model(data):
    """Model function."""
    df = pd.DataFrame(data)

    df1 = df.value_counts(subset=["make", "year"])

    df1




    
    return df, df1