import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

columnsbikebuyers = ["Marital Status", "Gender", "Income", "Children", "Education", "Occupation", "Home Owner", "Cars", "Commute Distance", "Region", "Age", "Purchased Bike"]
columnsbikebuyersfakedata = ["First Name", "Last Name", "Birthday", "Country", "City"]
df1 = pd.read_csv("assets/bike_buyers.csv", usecols=None)
df2 =pd.read_csv("assets/bike_buyers_fake_details.csv", usecols=None)

#currently says it's an empty data frame. Could have to do with usecols?
mergeddf = df1.merge(df2, left_on="Marital Status", right_on="First Name")
print(mergeddf)