import pandas as pd
from pandas import set_option
import numpy as np
import matplotlib.pyplot as plt
import os

set_option('display.max_rows', 10)

filename = open(os.path.expanduser("~/Downloads/data/gapminder.tsv"))
# filename = open(os.path.normpath("c:/users/jjenkins/downloads/data/gapminder.tsv"))
df = pd.read_table(filename,sep='\t')

print(df.head(2),'\n')

print(df.shape,'\n')
# tuple = rows x colums
# shape is an attribute of df not a fuction or method

print(df.columns,'\n')
print(df.dtypes,'\n')
# the object type and col names

print(df.info(),'\n')
# break down of info about the data from

# break up col by name
country_df = df['country']
print(country_df.head(2))
print(country_df.tail(2))

# use dot notation to call col attributes
country_df_dot = df.country
print(country_df_dot.head(2))

# stopped here
# https://youtu.be/7cpREpEPb_4?t=11m23s