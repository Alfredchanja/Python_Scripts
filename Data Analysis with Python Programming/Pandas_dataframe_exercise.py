'''
Alfred Gachanja
-12-2023
Exercise for pandas dataframes.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Creating a dataframe.
df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])
print(df)
print('\n')

# Creating an empty dataframe.
marvel = pd.DataFrame(
    data = [None],
    index = [None],
    columns = [None],
)
print("An empty DataFrame.")
print(marvel)

# Create a DataFrame called marvel_df with the given marvel data.
marvel_data = [
    ['Spider-man', 'male', 1962],
    ['Captain America','male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman','female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp','female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]
marvel = pd.DataFrame(data=marvel_data)
print(marvel)

# Add column names to the marvel DataFrame.
print('\n')
column_nms = ['name','sex','first_appearance']
marvel.columns = column_nms
print(marvel)
print('/n')

# Add index names to the marvel DataFrame.
marvel.index = marvel['name']
print(marvel)
print('\n')

# Drop the name column.
marvel = marvel.drop(['name'], axis = 1)
print(marvel)
print('\n')

# Drop 'Namor' and 'Hank Pym' rows.
marvel = marvel.drop(['Namor', 'Hank Pym'])
print(marvel)
print('\n')

# Show the first five elements of the marvel DataFrame.
print(marvel.iloc[0:5])
print('\n')

# Show the last five elements of the marvel DataFrame.
print(marvel.iloc[-5:])
print('\n')

# Show just the sex of the first 5 elements of the the marvel DataFrame.
print(marvel.iloc[:5] ['sex'].to_frame())
print('\n')

# Show the 'first_appearence' of all the middle elements of the marvel DataFrame.
print(marvel.iloc[1:-1] ['first_appearance'].to_frame())
print('\n')

# Show the first and the last element in the marvel DataFrame.
print(marvel.iloc[[0, 1]])
print('\n')

# Modify the first appearance of 'Vision to 1964.
marvel.loc['Vision', 'first_appearance']=1964
print(marvel)
print('\n')

# Add a new column called 'year since'.
marvel['year since'] = 2023 - marvel['first_appearance']
print(marvel)
print('\n')

# Make a mask showing the female characters.
female = marvel['sex'] =='female'
print(female)
print('\n')

# Get the male characters
male = marvel['sex'] == 'male'
print(marvel[male])
print('\n')

# Get the characters with the first appearance after 1970.
mask = marvel['first_appearance'] > 1970
print(marvel[mask])
print('\n')

# Get the female characters with the first appearance after 1970.
f_mask = (marvel['sex'] == 'female') & (marvel['first_appearance'] > 1970)
print(marvel[f_mask])
print('\n')

# Show the basic statistics of the marvel DataFrame
print(marvel.describe())
print('\n')

# Show the mean, min values of the first appearance.
print(marvel.first_appearance.mean())
print(marvel.first_appearance.min())
print('\n')

# Reset the index of the marvel DataFrame.
marvel = marvel.reset_index()
print(marvel)
print('\n')

#Plot the values of the first appearance.
plt.plot(marvel.index, marvel.first_appearance)
plt.hist(marvel.first_appearance)