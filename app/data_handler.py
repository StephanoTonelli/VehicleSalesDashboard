import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from config.auth import auth

data = pd.read_csv(auth)

df = pd.DataFrame(data)

df = df.dropna()
df = df.drop_duplicates()
df['Year_month'] = df['saledate'].astype('datetime64[ns, UTC]').dt.strftime("%Y-%m")


