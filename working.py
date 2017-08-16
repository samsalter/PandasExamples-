import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import os
# this will set panda to display a max of 16 rows
from pandas import set_option

set_option('display.max_rows', 20)

filename = open(os.path.expanduser("~/Downloads/data/annual.txt"))
# this brings in the file but will only load the data into 1 table
# the read_table assums your data will be seperated with a ','
# ull_globle_temp = pd.read_table(filename)

# this reads data but passes the seperator of any number of space
# we need to add colums to the table
# we will add a index instead of letting pandas do it
# we will set the year as the index which is under col=0
# you can have more than 1 index by setting more than 1 col
col = ['Year', 'Mean Temp']
ull_globle_temp = pd.read_table(filename, sep='\s+', names=col,
                                parse_dates=True, index_col=0)

print(ull_globle_temp)

# Bring in new table
# need to skip rows at the type and rows at the bottom
filename = open(os.path.expanduser("~/Downloads/data/glb.txt"))
giss_temp = pd.read_table(filename, sep='\s+', skiprows=7,
                          parse_dates=True, skip_footer=1, engine='python')
print(giss_temp)

filename = open(os.path.expanduser("~/Downloads/data/co2.txt"))
# parse_dates take 2 cols and combine them together
# to not combine [0,1]
co2_temp = pd.read_table(filename, sep='\s+', parse_dates=[[0, 1]], engine='python')
print(co2_temp)

# get data from web
url = 'http://sealevel.colorado.edu/files/current/sl_nh.txt'
sl_nh = pd.read_table(url, sep='\s+', engine='python')
print(sl_nh)

url = 'http://sealevel.colorado.edu/files/current/sl_sh.txt'
sl_sh = pd.read_table(url, sep='\s+', engine='python')
print(sl_sh)

url = 'http://sealevel.colorado.edu/files/2016_rel4/sl_ns_global.txt'
sl_global = pd.read_table(url, sep='\s+', engine='python')
print(sl_global)

# parse a html file and only brings back tables as your data frame
url = 'http://www.psmsl.org/data/obtaining/'
table_list = pd.read_html(url)
print(len(table_list))
print(table_list)
sl_ls = table_list[0]
print(sl_ls)

# type of object = class 'pandas.core.frame.DataFrame'
print(type(giss_temp))

# internal nature of the object
print(giss_temp.shape)  # tell you rows, col
print(giss_temp.dtypes)  # tell data type of col "object = general

# show index and col
print(giss_temp.index)
print(giss_temp.columns)

print(giss_temp.info())

# working with 1D structure called series, #move from a datafrom to series
print(type(ull_globle_temp))

print(ull_globle_temp.columns)
ull_globle_temp = ull_globle_temp['Mean Temp']

print(type(ull_globle_temp))
print(ull_globle_temp.dtype)
print(ull_globle_temp.shape)  # shape only has 1 object
print(ull_globle_temp.nbytes)  # shows the memory footprint

print(ull_globle_temp.head())
print(ull_globle_temp.tail())

print(ull_globle_temp.index)

# Manually create a dataframe // to have two series share 1 datafram the indexes must
# be algined
print(sl_sh.columns)
print(sl_sh.year == sl_nh.year)

# to grab the a col in a series/DF use the [ ]
# print(sl_sh['year']) you can use this or the dot notation listed above

# same as above just using the numpy to do it
print(np.all(sl_sh.year == sl_nh.year))

# lets make a datafram using a dic from the series/col
mean_sea_level = pd.DataFrame({"northern_hem": sl_nh['msl_ib(mm)'],
                               "southern_hem": sl_sh['msl_ib(mm)'],
                               "date": sl_sh['year']})
print(mean_sea_level)

# same as above but created with year as index and remove it from the
mean_sea_level = pd.DataFrame(dict(northern_hem=sl_nh['msl_ib(mm)'], southern_hem=sl_sh['msl_ib(mm)']),
                              index=sl_nh.year)
print(mean_sea_level)

# the series above index is not related to the index we want for the dataframe
# so instead ask values since we know the data matches
mean_sea_level = pd.DataFrame(dict(northern_hem=sl_nh['msl_ib(mm)'].values,
                                   southern_hem=sl_sh['msl_ib(mm)'].values),
                              index=sl_nh.year)
print(mean_sea_level)

# cleaning and formatting data
print(sl_ls.columns)

# using a list comprehensions It can be used to construct lists in a very natural, easy way,
# like a mathematician is used to do.

sl_ls.columns = [name.strip().replace(".", "") for name in sl_ls.columns]
print(sl_ls.columns)

# we can also rename indexs also
mean_sea_level.index.name = 'date'
print(mean_sea_level.index.name)

# if there are missing value this can handle it
# np.nan is a value in numpy that would do this.

# will search for this value and mark it as turn
ull_globle_temp == -999.000

ull_globle_temp[ull_globle_temp == -999.000] = np.nan
ull_globle_temp.tail()

# Stopped at 2:01:33
# https://youtu.be/0CFFTJUZ2dc?t=2h1m33s