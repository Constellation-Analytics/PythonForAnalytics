
# -------------------------------------------------------------------
#                         Data Cleaning
# -------------------------------------------------------------------
import streamlit as st
st.header("🧹 Data Cleaning")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Dealing with Missing Data
- Dealing with Duplicate Data
"""
)
st.subheader("Dropping NA values above a specified threshhold")
st.code(
"""
# Define the acceptable threshold
threshold = len(df) * 0.05

# Create a filter to identify columns that have more NA values than the threshold
columns_above_threshold = df.columns[df.isna().sum() >= threshold]

# Drop NA values within columns above the threshold
df.dropna(subset=columns_above_threshold, inplace=True)
""")

st.subheader("Filling NA values with a summary statistic - Basic")
st.code(
"""
# Numeric: Fill with mean
df['numeric_column'] = df['numeric_column'].fillna(df['numeric_column'].mean())

# Categorical: Fill with mode
df['categorical_column'] = df['categorical_column'].fillna(df['categorical_column'].mode()[0])
""")

st.subheader("Filling NA values with a summary statistic - Advanced")
st.code(
"""
# Create a list of the columns to treat based on a condition
cols_with_missing_values = df.columns[df.isna().sum() > 0]
# OR
# Select specific columns
cols_with_missing_values = ['column1', 'column2']

# Fill the NA values by using the 1st mode found
# (Always index reference the mode in case there are multiple modes)
for col in cols_with_missing_values:
    df[col].fillna(df[col].mode()[0], inplace=True)

""")

st.subheader("Filling NA values by subgroup")
st.code(
"""
# Create a dictionary of median values for a subgroup
my_dict = df.groupby("subgroup")["column1"].median().to_dict()

# Fill the NA values by mapping them to the dictionary 
df["column1"] = df["column1"].fillna(df["subgroup"].map(my_dict)
""")

st.subheader("Identifying Duplicate Rows")
st.code(
"""
# Identify duplicate rows
duplicate_rows = df[df.duplicated()]

# Identify duplicate rows based on specific columns
duplicate_rows_subset = df[df.duplicated(subset=['column1', 'column2'])]
"""
)

st.subheader("Dropping Duplicate Rows")
st.code(
"""
# Drop duplicate rows and keep the first occurrence
df.drop_duplicates(inplace=True)

# Drop duplicate rows based on specific columns and keep the last occurrence
df.drop_duplicates(subset=['column1', 'column2'], keep='last', inplace=True)
"""
)

st.subheader("Flagging Duplicate Rows")
st.code(
"""
# Create a new column to flag duplicates
df['is_duplicate'] = df.duplicated()

# Flag duplicates based on specific columns
df['is_duplicate'] = df.duplicated(subset=['column1', 'column2'])
"""
)
