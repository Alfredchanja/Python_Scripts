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
  average_age_men = df[['sex', 'age']][df['sex'] == 'Male']['age'].mean()

  # Average age of females.
  # average_age_women = df[['sex', 'age']][df['sex'] == 'Female']['age'].mean()

  print(average_age_men)
  # print(average_age_women)
  # print(df.isnull())
  # print(df.notnull())
  # print(df.info())
  # print(df.shape)
  # print(df.isnull().sum())
  # print(df.notna().sum())
  # print(df.any())
  # print(df.all())
  # print(df['sex'].unique())
  # print(df['sex'].value_counts())
  # print(df['race'].unique())
  # print(df['race'].value_counts())
calculate_demographic_data()