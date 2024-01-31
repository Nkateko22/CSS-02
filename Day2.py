# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:47:37 2024

@author: nkate
"""

import pandas as pd

file =pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/iris.csv")

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

url = "https://raw.githubusercontent.com/kode2go/nithecs/main/lecture_01/iris.csv"

file = pd.read_csv(url)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

file = pd.read_csv(url, header=None, names= column_names)

file = pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/Geospatial Data.txt",sep=";")

file = pd.read_excel("C:/Users/nkate/Downloads/NK/.spyproject/data_02/residentdoctors.xlsx")

file = pd.read_json("C:/Users/nkate/Downloads/NK/.spyproject/data_02/student_data.json")

print(file)


file =pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/country_data_index.csv")
df =pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/country_data_index.csv", index_col=0)


df = pd.read_excel("C:/Users/nkate/Downloads/NK/.spyproject/data_02/residentdoctors.xlsx")

# Step 1: Extract the lower end of the age range (digits only)
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')

# Step 2: Convert the new column to float
df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)

print(df.info())

x = {'a': 1, 'b': 2}
x.update({'c': 3})

x = {'a': 1, 'b': 2}
del x['a']
print(x)

x = [1,2,3]
y = x[1:]
print(y)

"""
Working with dates
"""

10-01-2024 - UK
01-10-2024 - US


df = pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/time_series_data.csv")
df = pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/time_series_data.csv", index_col=0)


print (df.info())
# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Split the 'Date' column into separate columns for year, month, and day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

df['Date'].dt.year
df['Date'].dt.month
df['Date'].dt.day

df

import pandas as pd

df = pd.read_csv('C:/Users/nkate/Downloads/NK/.spyproject/data_02/patient_data_dates.csv')
df = pd.read_csv('C:/Users/nkate/Downloads/NK/.spyproject/data_02/patient_data_dates.csv', index_col=0)

# Allows you to see all rows
df.drop(index=26, inplace=True)
df.dropna(inplace = True)
df = df.reset_index(drop=True)
df['Duration'] = df['Duration'].replace([450], 50)
print (df)

#################################################

df=pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/iris.csv")

print(df.columns)

col_names =df.columns

print(col_names)

grouped = df.groupby("class")

# Calculate mean, sum, and count for the squared values
mean_squared_values = grouped['sepal_length'].mean()
sum_squared_values = grouped['sepal_length'].sum()
count_squared_values = grouped['sepal_length'].count()

print("Mean of Sepal Length Squared:")
print(mean_squared_values)

print("\nSum of Sepal Length Squared:")
print(sum_squared_values)

print("\nCount of Sepal Length Squared:")
print(count_squared_values)

################################

# Read the CSV files into dataframes
df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")

# Concatenate the dataframes
df = pd.concat([df1, df2], ignore_index=True)

df1 = pd.read_csv('data_02/person_education.csv')
df2 = pd.read_csv('data_02/person_work.csv')

## inner join
df_merge = pd.merge(df1,df2,on='id')

df_merge = pd.merge(df1, df2, on='id', how='outer')


file =pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/iris.csv")
pd=pd.read_csv("C:/Users/nkate/Downloads/NK/.spyproject/data_02/iris.csv")

pd["class"] =pd["class"].str.replace("Iris-","")

df =df[df['sepal_length']>5]

pd = pd[pd["class"] == "virginica"]

df.to_csv("pulsar.csv")
