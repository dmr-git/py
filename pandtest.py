#!/usr/bin/env python3

import numpy as np
import pandas as pd
import os


my_array = np.random.rand(3)
print("my_array:")
print(my_array)
print(type(my_array))
print(f"my_array[0] = {my_array[0]}")
print()

my_series = pd.Series(np.random.rand(3))
print("my_series:")
print(my_series)
print(type(my_series))
print(f"my_series[0] = {my_series[0]}")
print()

my_series = pd.Series(np.random.rand(3), index=["First", "Second", "Third"])
print("my_series with labels:")
print(my_series)
print(type(my_series))
print(f'my_series["Second"] = {my_series["Second"]}')
print(f'my_series[1] = {my_series[1]}')
print(f'my_series.index = {my_series.index}')
print()

array_2d = np.random.rand(3,2)
print("array_2d:")
print(array_2d)
print(f"array_2d[1,1] = {array_2d[1,1]}")      
print()

my_df = pd.DataFrame(array_2d)
my_df.columns = ["First", "Second"]
print("my_df:")
print(my_df)
print(type(my_df))
print()

print('my_df["Second"]: (this is now a Series or slice of the DataFrame)')
print(my_df["Second"])
print(type(my_df["Second"]))
print()

# where the data file is
CSV_PATH = os.path.join('~/code', 'data', 'artwork_data.csv')

# read just 5 rows to see what the data is
df = pd.read_csv(CSV_PATH, nrows=5, index_col='id')

print(df.head)
print(df.dtypes)
print()

COLS_TO_USE = ['id', 'artist', 'title',
               'medium', 'year', 'acquisitionYear',
               'height', 'width', 'units']

df = pd.read_csv(CSV_PATH, nrows=5,
                 index_col='id',
                 usecols=COLS_TO_USE)

print(df.head)
