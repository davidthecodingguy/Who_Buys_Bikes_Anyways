import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

columnsbikebuyers = ["ID","Marital Status", "Gender", "Income", "Children", "Education", "Occupation", "Home Owner", "Cars", "Commute Distance", "Region", "Age", "Purchased Bike"]
columnsbikebuyersfake = ["First Name", "Last Name", "Birthday", "Country", "City"]
df = pd.read_csv("assets/bike_buyers.csv", usecols=columnsbikebuyers)
df2 =pd. read_csv("assets/bike_buyers_fake_details.csv", usecols=columnsbikebuyersfake)
print(df, df2)