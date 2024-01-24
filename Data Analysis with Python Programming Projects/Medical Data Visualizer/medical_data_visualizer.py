"""
Alfred Gachanja
24-01-2024
This program shows a visual representation of some medical data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column.
BMI = (df['weight']/((df['height'])/100)**2)
df['overweight'] = np.where(BMI > 25, 1, 0)

print(df.head())