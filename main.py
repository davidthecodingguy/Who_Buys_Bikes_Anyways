import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#reading in two data files. Feature #1
columnsbikebuyers = ["Marital Status", "Gender", "Income", "Children", "Education", "Occupation", "Home Owner", "Cars", "Commute Distance", "Region", "Age", "Purchased Bike"]
columnsbikebuyersfakedata = ["Birthday", "Country", "City", "Marital Status"]
df1 = pd.read_csv("assets/bike_buyers.csv", usecols=columnsbikebuyers)
df2 =pd.read_csv("assets/bike_buyers_fake_details.csv", usecols=columnsbikebuyersfakedata)

#clean and Pandas merge. Feature #2
df1.dropna(inplace=True)
df2.replace(to_replace=1.0, value="Married", inplace=True)
df2.fillna("Single", inplace=True)
merged_df = df1.merge(df2, left_on="Marital Status", right_on="Marital Status")

#TESTING FUNCTIONALITY, WILL DELETE LATER
print(merged_df)
