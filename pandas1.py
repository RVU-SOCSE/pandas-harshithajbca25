import pandas as pd

# Create a DataFrame using a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 90, 78],
    'Age': [20, 21, 19]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Add a new column with calculated values (e.g., Marks + 5 bonus)
df['Updated Marks'] = df['Marks'] + 5

# Display the updated DataFrame
print("\nDataFrame after adding new column:")
print(df)
