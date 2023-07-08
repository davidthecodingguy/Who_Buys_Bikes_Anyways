import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#reading in two data files. Feature #1
columns_bike_buyers = ["Marital Status", "Gender", "Income", "Children", "Education", "Occupation", "Home Owner", "Cars", "Commute Distance", "Region", "Age", "Purchased Bike"]
columns_bike_buyers_fake_data = ["Birthday", "Country", "City", "Marital Status"]
df1 = pd.read_csv("assets/bike_buyers.csv", usecols=columns_bike_buyers)
df2 = pd.read_csv("assets/bike_buyers_fake_details.csv", usecols=columns_bike_buyers_fake_data)

#clean and Pandas merge. Feature #2
df1.dropna(inplace=True)
df2.replace(to_replace=1.0, value="Married", inplace=True)
df2.fillna("Single", inplace=True)
merged_df = df1.merge(df2, left_on="Marital Status", right_on="Marital Status")

occupational_pivot_table = pd.pivot_table(merged_df, index=["Occupation", "Purchased Bike", "Education"], aggfunc={"Income": np.mean, "Age": np.mean})
#TESTING FUNCTIONALITY, WILL DELETE LATER
print(occupational_pivot_table)
#print(merged_df)
