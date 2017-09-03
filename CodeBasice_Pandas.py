import pandas as pd

# Creating dataframe
#  data frame is all about row and col

df = pd.read_csv('Data\weather_data.csv')
print(df) # Print the dataframe

#create a data frame using a dict
weather_data ={ 'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
                'temp': [32,35,28,24,32,31],
                 'windspeed': [6,7,2,7,4,2],
                  'event': ['rain','sunny','snow','snow','rain','sunny']
                }
# day,temp,windspeed, event = keys in my dic
# move it to a data fram
dic_df = pd.DataFrame(weather_data)
print(dic_df)
# dealing with rows and columns
# lets print the shape which is the # of rows col
print(df.shape) # this is a tuple in python
row, col = df.shape
print(row)
print(col)

# print small sample of data
print(df.head(2)) # print first 2 leave blank brings back 5-10
print(df.tail() ) # print last value

# to print from row x to y
print(df[2:5]) # prints row 2 - 4  df[:] will give you everything

print(df.columns) # gives you the list of col names
print(df.windspeed) # will give you that col data
print(df['day']) # will do the same as above

print(type(df.event))

# print only the col you want
print(df[['event','day']])

# Operations min, max, std, describe
print(df.temperature.max())
print(df.temperature.min())
print(df.temperature.std())

# print the stats of the data col with numbers
print(df.describe())

# conditional selection
# almost like SQL
print(df[df.temperature>31])

# brings back the max row in data frame
print(df[df.temperature==df.temperature.max()])
# gets the max row but only bring back the day and temp
print(df[['day','temperature']][df.temperature==df['temperature'].max()])


# set the index
print(df.index)

# df.set_index('day') # this will give you a new data frame with an index of day
df.set_index('day',inplace=True)
print(df.index)
print(df.loc['1/2/2017'])

# to reset the index
df.reset_index(inplace=True)
