# %%
#1. Pandas is a powerful Python library for data manipulation and analysis, 
# offering data structures like DataFrames for tabular data, similar to Excel spreadsheets. 
# Pandas is widely used for its ease of use, flexibility, and speed in handling large datasets.

#2. Give an example of how to import a csv file using pandas
import pandas as pd
df = pd.read_csv('data.csv')

#3.Show how to view the first 10 rows of a dataset using pandas
df.head(10)

#4.Write a Pandas program to compare the elements of the two Pandas Series.
#Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

import pandas as pd
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
series1 == series2

#5. Change the first character of each word to upper case in each word of df1
# df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
df1.str.capitalize()


