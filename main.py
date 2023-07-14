import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Feature #1: Reading in two data files
columns_bike_buyers = ["ID","Marital Status", "Gender", "Income", "Children", "Education", "Occupation", "Home Owner", "Cars", "Commute Distance", "Region", "Age", "Purchased Bike"]
columns_bike_buyers_fake_data = ["ID", "Birthday", "Country", "City", "Marital Status"]
df1 = pd.read_csv("assets/bike_buyers.csv", usecols=columns_bike_buyers)
df2 = pd.read_csv("assets/bike_buyers_fake_details.csv", usecols=columns_bike_buyers_fake_data)

#Feature #2: Clean data and merge data dataframes using Pandas.
#Replacing "No" values with NaN to filter "Purchased Bike" results in cleaned dataframe and drop blank values from df1
df1.replace(to_replace="No", value=pd.np.nan, inplace=True)
df1.dropna(inplace=True)
#"Marital Status" column in df2 is inaccurate/confusing and is cleaned from dataset
df2.drop("Marital Status", inplace=True, axis=1)
df2.dropna(inplace=True)
merged_df = df1.merge(df2, left_on="ID", right_on="ID")

#Feature #3: Creating pivot tables and visualizing data with bar graphs
job_pt = pd.pivot_table(merged_df, index=["Occupation"], aggfunc={"Income": [max, np.mean, min]}).plot.barh(figsize=(10,7), title="Bike Purchaser Occupation Types and their Incomes", xlabel=("Income Levels"))
job_pt.legend(title="Reported Income", labels=["Max", "Average", "Minimum"])
commute_pt = pd.pivot_table(merged_df, index=[ "Commute Distance"], aggfunc={"Cars": [max, np.mean, min]}).plot.barh(figsize=(10,7), title="Bike Purchaser Commute Distances and their Cars Owned", xlabel=("Cars Per Household"))
commute_pt.legend(title="Cars Owned", labels=["Most", "Average", "Least"])
education_pt = pd.pivot_table(merged_df, index=["Education"], aggfunc={"Income": [max, np.mean, min]}).plot.barh(figsize=(10,7), title="Bike Purchaser Education Levels and their Incomes", xlabel=("Income Levels"))
education_pt.legend(title="Reported Income", labels=["Max", "Average", "Minimum"])

#Data visualization that allows users to click through tabs to see different data views
plt.rcParams["figure.autolayout"] = True
plt.show()
