import pandas as pd
import os
from pandas import set_option
import matplotlib


set_option('display.max_rows', 10)


filename = open(os.path.expanduser("~/Downloads/data/titanic3.csv"))

df = pd.read_csv(filename)
print(df.info())

print(df.survived.value_counts())

# EDA
# learn about the data
# is it categorical what are categories
# can put in cat what is min, max
# missing values
# distribution of variable

print(df.sex.value_counts())

df.sex.value_counts().plot(kind='bar')


print(df[df.sex=='female'])
