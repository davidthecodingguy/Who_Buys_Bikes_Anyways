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

#pivot tables. Part of Feature #3
job_pt = pd.pivot_table(merged_df, index=["Occupation", "Purchased Bike"], aggfunc={"Income": [max, np.mean, min]})
commute_pt = pd.pivot_table(merged_df, index=[ "Commute Distance", "Purchased Bike"], aggfunc={"Age": [max, np.mean, min], "Cars": [max, min]})
education_pt = pd.pivot_table(merged_df, index=["Education", "Purchased Bike"], aggfunc={"Age": [max, np.mean, min]})
marital_pt = pd.pivot_table(merged_df, index=["Purchased Bike", "Marital Status"], aggfunc={"Age": [max, np.mean, min]})
country_pt = pd.pivot_table(merged_df, index=["Purchased Bike", "Country"], aggfunc={"Age": [max, np.mean, min]})

#TESTING FUNCTIONALITY, WILL DELETE LATER
print(job_pt)
print(commute_pt)
print(education_pt)
print(marital_pt)
print(country_pt)
#print(merged_df)
