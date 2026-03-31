import pandas as pd

#Load the CSV file
df = pd.read_csv('data.csv')

#Display the DataFrame
print("Original DataFrame:")
print(df)

#Identify missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

#Fill missing values with mean (for numeric columns only)
df_filled = df.fillna(df.mean(numeric_only=True))

#Display updated DataFrame
print("\nDataFrame after filling missing values with mean:")
print(df_filled)
