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
  average_age_men = df[['sex', 'age']][df['sex'] == 'Male']['age'].mean().round(1)

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

  # What is the percentage of people who have a Bachelor's degree.
  percentage_bachelors = ((df['education'] == 'Bachelors').mean() * 100).round(1)

  print(percentage_bachelors)

  # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

    # With and without 'Bachelors', 'Masters', or 'Doctorate'
  
  higher_education = df['education'][(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
  lower_education = df['education'][(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]

  # print(higher_education.count())
  # print(lower_education.count())

  # Percentage with salary greater than 50k.
  higher_education_rich = ((df[df['education'].isin(higher_education) & 
    (df['salary'] == '>50K')]['salary'].count() / df[df['education'].isin(higher_education)]['salary'].count() * 100)).round(1)
  
        # Alternative code
        # higher_education_rich = df[['education', 'salary']][((df['education'] == 'Bachelors') | 
        #   (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')]
        #   ['salary'].count() * 100 / df[['education', 'salary']][(df['education'] == 'Bachelors') | 
        #   (df['education'] == 'Masters') | (df['eduzcation'] == 'Doctorate')]['salary'].count()

  lower_education_rich = (df[['education', 'salary']][((df['education'] != 'Bachelors') & 
    (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & 
    (df['salary'] == '>50K')]['salary'].count() * 100 / df[['education', 'salary']][(df['education'] != 'Bachelors') & 
    (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]['salary'].count()).round(1)

  print(higher_education_rich)
  print(lower_education_rich)

  # What is the minumum number of hours a person works per week?
  min_work_hours = df['hours-per-week'].min()

  total = df['hours-per-week'][df['hours-per-week'] == min_work_hours].count()

  # What percentage of people who work the minimum number of hours per week have a salary of more than 50k.

  num_min_workers = (df[['hours-per-week', 'salary']][(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]['salary'].count() * 100 / total).round(1)

  print(min_work_hours)
  print(total)
  print(num_min_workers)
  
  # What country has the highest percentage of people that earn >50K and what is that percentage.
  highest_income_df = df[df['salary'] == '>50K']
  highest_earning_country = (highest_income_df[['native-country','salary']]['native-country'].value_counts()/df['native-country'].value_counts() * 100).idxmax()
  highest_earning_country_percentage = (highest_income_df[['native-country','salary']]['native-country'].value_counts()/df['native-country'].value_counts() * 100).max().round(1)

  # print(highest_income_df)
  print(highest_earning_country)
  print(highest_earning_country_percentage)
  
calculate_demographic_data()