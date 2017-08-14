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
#ull_globle_temp = pd.read_table(filename)

#this reads data but passes the seperator of any number of space
# we need to add colums to the table
# we will add a index instead of letting pandas do it
# we will set the year as the index which is under col=0
# you can have more than 1 index by setting more than 1 col
col = ['Year','Mean Temp']
ull_globle_temp = pd.read_table(filename, sep='\s+', names=col,
                  parse_dates=True, index_col=0 )

print(ull_globle_temp)

#Bring in new table
# need to skip rows at the type and rows at the bottom
filename = open(os.path.expanduser("~/Downloads/data/glb.txt"))
giss_temp = pd.read_table(filename, sep='\s+', skiprows=7,
                  parse_dates=True, skip_footer=1,engine='python')
print(giss_temp)


filename = open(os.path.expanduser("~/Downloads/data/co2.txt"))
#parse_dates take 2 cols and combine them together
#to not combine [0,1]
co2_temp = pd.read_table(filename, sep='\s+',parse_dates=[[0,1]],engine='python')
print(co2_temp)

# get data from web
url = 'http://sealevel.colorado.edu/files/current/sl_nh.txt'
sl_nh = pd.read_table(url, sep='\s+',engine='python')
print(sl_nh)

url = 'http://sealevel.colorado.edu/files/current/sl_sh.txt'
sl_sh = pd.read_table(url, sep='\s+',engine='python')
print(sl_sh)

url = 'http://sealevel.colorado.edu/files/2016_rel4/sl_ns_global.txt'
sl_global = pd.read_table(url, sep='\s+',engine='python')
print(sl_global)

#parse a html file and only brings back tables as your data frame
url = 'http://www.psmsl.org/data/obtaining/'
#table_list = pd.read_html(url)
#print(len(table_list))
#print(table_list)
#sl_ls = table_list[0]
#print(sl_ls)

#type of object = class 'pandas.core.frame.DataFrame'
print(type(giss_temp))

# internal nature of the object
print(giss_temp.shape) # tell you rows, col
print(giss_temp.dtypes) # tell data type of col "object = general

# show index and col
print(giss_temp.index)
print(giss_temp.columns)

print(giss_temp.info())

#working with 1D structure called series
print(type(ull_globle_temp))
