import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

#Feature #1: Reading in two data files
columns_bike_buyers = ["Marital Status", "Gender", "Income", "Children", "Education", "Occupation", "Home Owner", "Cars", "Commute Distance", "Region", "Age", "Purchased Bike"]
columns_bike_buyers_fake_data = ["Birthday", "Country", "City", "Marital Status"]
df1 = pd.read_csv("assets/bike_buyers.csv", usecols=columns_bike_buyers)
df2 = pd.read_csv("assets/bike_buyers_fake_details.csv", usecols=columns_bike_buyers_fake_data)

#Feature #2: Clean data and merge data dataframes using Pandas
df1.replace(to_replace="No", value=pd.np.nan, inplace=True)
df1.dropna(inplace=True)
df2.replace(to_replace=1.0, value="Married", inplace=True)
df2.fillna("Single", inplace=True)
merged_df = df1.merge(df2, left_on="Marital Status", right_on="Marital Status")

#Feature #3: Creating pivot tables and visualizing data with bar graphs
job_pt = pd.pivot_table(merged_df, index=["Occupation"], aggfunc={"Income": [max, np.mean, min]}).plot.barh(figsize=(10,7), title="Bike Purchaser Occupation Types and their Incomes")
job_pt.legend(title="Income Levels", labels=["Max", "Average", "Minimum"])
commute_pt = pd.pivot_table(merged_df, index=[ "Commute Distance"], aggfunc={"Cars": [max, np.mean, min]}).plot.barh(figsize=(10,7), title="Bike Purchaser Commute Distances and their Cars Owned")
commute_pt.legend(title="Cars Owned", labels=["Most", "Average", "Least"])
education_pt = pd.pivot_table(merged_df, index=["Education"], aggfunc={"Income": [max, np.mean, min]}).plot.barh(figsize=(10,7), title="Bike Purchaser Education Levels and their Incomes")
education_pt.legend(title="Income Levels", labels=["Max", "Average", "Minimum"])

#Data visualization that allows users to click through tabs to see different data views
plt.rcParams["figure.autolayout"] = True
plt.show()
