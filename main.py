import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

columnsbikebuyers = ["Marital Status", "Gender", "Income", "Children", "Education", "Occupation", "Home Owner", "Cars", "Commute Distance", "Region", "Age", "Purchased Bike"]
columnsbikebuyersfakedata = ["Birthday", "Country", "City", "Marital Status"]
df1 = pd.read_csv("assets/bike_buyers.csv", usecols=columnsbikebuyers)
df2 =pd.read_csv("assets/bike_buyers_fake_details.csv", usecols=columnsbikebuyersfakedata)
#need to change integers to strings in Marital Status column. Might fix error. Python advises to use pd.concat. This also gives an error
merged_df = pd.merge(df1, df2)
#merged_df = df1.merge(df2, left_on="Marital Status", right_on="Marital Status")
print("df1", "df2", merged_df)