## Import os for checking the working directory 
## and pandas for working with data frames

import os
import pandas as pd

# Check working directory
os.getcwd()

# Use pandas to read in the raw csv file to a dataframe object
df = pd.read_csv('ga_jan19_ri_ny.csv')

# View new data frame
print(df)

# Convert "Date" column in df dataframe object to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Set the date column as the index
df.set_index(df["Date"],inplace=True)

# Group daily Date values by Week instead, with a Thursday week-end date
df_a = df.resample('W-THU').sum()

# Plot pageviews by week for the geo segment
df_a.plot(y="PageViews",title='PageViews by Week for RI and NY - January 2019')

