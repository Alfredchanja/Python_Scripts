"""
Alfred Gachanja
10-01-2024
This program analyzes demographic data using pandas.
"""

import pandas as pd

def calculate_demographic_data():

  # Read data from the file.
  df = pd.read_csv('adult.data.csv')
  # print(df.head())
  # print(df.info())

  # How many people of each race are represented in this dataset?
  #  This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # print(race_count)

  # What is the average age of men
  # average_age_men = df['age'].mean()

  # print(average_age_men)

calculate_demographic_data()