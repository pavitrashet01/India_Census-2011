# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:59:46 2026

@author: pavitra
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\pavitra\Desktop\Census_data analysis\Census_dataset.csv")

print("India Census 2011 Dataset")
print(df)

df.head()
df.shape
df.info()
df.dtypes
df.describe()
df.duplicated().sum()
df.isnull().sum()
df.columns


'Create New Columns (Feature Engineering)'

# Literacy Rate
df['Literacy_Rate'] = (df['Literate'] / df['Population']) * 100
df['Literacy_Rate']


# Sex Ratio
df['Sex_Ratio'] = (df['Female'] / df['Male']) * 1000
df['Sex_Ratio']


'Filtering Data'

# Districts with Population > 1 Million
high_population = df[df['Population'] > 1000000]

print("\nDistricts with Population > 1 Million")
print(high_population[['State_name','District_name','Population']])


# Districts with High Literacy
high_literacy = df[df['Literacy_Rate'] > 80]

print("\nHigh Literacy Districts")
print(high_literacy[['District_name','Literacy_Rate']])


'Aggregation'

# Total Population by State
state_population = df.groupby('State_name')['Population'].sum()

print("\nTotal Population by State")
print(state_population)


# Average Literacy by State
state_literacy = df.groupby('State_name')['Literacy_Rate'].mean()

print("\nAverage Literacy Rate by State")
print(state_literacy)



'Sorting'

# Top 10 Most Populated Districts
top_population = df.sort_values(by='Population', ascending=False).head(10)

print("\nTop 10 Most Populated Districts")
print(top_population[['District_name','Population']])



'Visualization'

# Top 10 States by Population
state_population.sort_values(ascending=False).head(10).plot(kind='bar')

plt.title("Top 10 States by Population")
plt.ylabel("Population")

plt.show()



# Top 10 Population Districts (Bar Chart)
top_population.plot(
    x='District_name',
    y='Population',
    kind='bar',
    title='Top 10 Districts by Population'
)

plt.xticks(rotation=60)
plt.show()



# Literacy Rate Distribution (Histogram)
plt.hist(df['Literacy_Rate'], bins=20)

plt.title("Literacy Rate Distribution")
plt.xlabel("Literacy Rate")
plt.ylabel("Frequency")

plt.show()



# Male vs Female Population (Scatter Plot)
plt.scatter(df['Male'], df['Female'])

plt.title("Male vs Female Population")
plt.xlabel("Male Population")
plt.ylabel("Female Population")

plt.show()



