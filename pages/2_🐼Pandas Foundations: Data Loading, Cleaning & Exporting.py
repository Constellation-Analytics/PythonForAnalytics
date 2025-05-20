import streamlit as st
st.header("🐼 Data Manipulation with Pandas")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Loading Data with Pandas
- Inspecting Data
- Selecting, Filtering, and Sorting Data
- Adding, Removing, and Renaming Columns
- Exporting Data with Pandas
""")

# Loading Data with Pandas          
st.subheader("Loading Data with Pandas")
st.code("""
import pandas as pd

file = str(input("Please enter a file"))
file = file.replace('"','')
#OR
file = (r"your_file_path")    
            
# Reading a CSV file:
df = pd.read_csv(file)

#Reading an Excel file
df = pd.read_excel(file)      
    """)

# Inspecting Data        
st.subheader("Inspecting Data")
st.code("""
import pandas as pd

# Return the first 10 rows
print(df.head())

# Return basic info including [Column, Non-Null Count, Dtype]
print(df.info())

# Return summary statistics for numeric columns [Count, Meam, Std, Min, Max, etc]
print(df.describe())

# Return a list of the columns in the dataset
print(df.columns)
    """)

# Selecting, Filtering, and Sorting Data
st.subheader("Selecting, Filtering, and Sorting Data")
st.code("""
import pandas as pd
            
# Selecting rows based on boolean condition
filtered_df = df[df['column'] > 10]

# Select specific columns
selected_columns = df[['column1', 'column2']]
            
# Selecting rows and columns based on boolean condition
selected_data = df[df['column'] > 10][['column1', 'column2']]

# Selecting specific rows and columns using loc
selected_data = df.loc[df['column'] > 10, ['column1', 'column2']]
            
# Using iloc (Integer-location based indexing)
df.iloc[1:3, 0:2])  # Rows 1 to 2, columns 0 to 1

# Creating a boolean filter and passing this to the dataframe
filtered_values = (employees['department'] == 'HR') & (employees['salary'] > 50000)
hr_high_salary = employees[filtered_values]

# Sorting Data
df = df.sort_values(by='column1', ascending=False)
#OR multiple columns
df = df.sort_values(by = ['column1','column2'])

    """)

# Filtering with .isin()
st.subheader("Filtering with .isin()")
st.code("""
import pandas as pd
            
# List of names to filter
names_to_include = ['Alice', 'David']

# Filter DataFrame to include only specified names
filtered_df = df[df['Name'].isin(names_to_include)]
            
# List of names to exclude
names_to_exclude = ['Alice', 'David']

# Filter DataFrame to exclude specified names. 
# Notice this symbol ( ~ ) negates .isin() to make it "is NOT in"
filtered_df = df[~df['Name'].isin(names_to_exclude)]
        
    """)

# Adding, Removing, and Renaming Columns         
st.subheader("Adding, Removing, and Renaming Columns")
st.code("""
import pandas as pd

# Adding New Columns
df['new_column'] = df['column1'] + df['column2']

# Removing Columns
df = df.drop(columns=['unwanted_column'])

# Renaming Columns option #1
df = df.rename(columns={'old_name': 'new_name'})

# Renaming Columns option #2
df.columns = ['column1_name', 'column2_name']

    """)

# Exporting Data with Pandas         
st.subheader("Exporting Data with Pandas")
st.code("""
import pandas as pd

# Writing to a CSV file
df.to_csv('output.csv', index=False)

# Writing to an Excel file
df.to_excel('output.xlsx', index=False        
    """)
