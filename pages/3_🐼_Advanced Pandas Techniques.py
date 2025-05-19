# -------------------------------------------------------------------
#                         Data Manipulation 2 
# -------------------------------------------------------------------
import streamlit as st
st.header("🐼 Advanced Pandas Techniques")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Grouping Data
- Aggregating Data with .Agg()
- Creating Pivot Tables
- Joining DataFrames
- Reshaping Data: melt (Comming soon)
- Concatenating and Appending DataFrames (Comming soon)

"""
)

# Grouping and Aggregating Data
st.subheader("Grouping Data")
st.code(
"""
import pandas as pd

# Calculate median for all numeric columns
df.groupby("category").median().reset_index()

# Calculate median for a specific numeric column
grouped_data = df.groupby("category")["numeric_column"].median().reset_index()

# Grouping with multiple aggregation types
grouped_data = df.groupby("category").agg(
    sum=("numeric_column", "sum"),
    mean=("numeric_column", "mean"),
    count=("numeric_column", "count"),
    min=("numeric_column", "min"),
    max=("numeric_column", "max"),
    median=("numeric_column", "median"),
    std=("numeric_column", "std"),
    var=("numeric_column", "var"),
    first=("numeric_column", "first"),
    last=("numeric_column", "last")
).reset_index()
""")

st.subheader("Aggregating Data with .Agg()")
st.code(
"""
import pandas as pd

# Aggregating all numeric columns across a DataFrame
df.agg(["mean", "std"])

# Aggregating specific columns across a DataFrame
df.agg({"numeric_column_1": ["mean", "std"], "numeric_column_2": ["median"]})

""")

st.subheader("Creating Pivot Tables")
st.code("""
import pandas as pd

# Pivot table - pivot_table always takes the mean by default. 
df = df.pivot_table(values='numeric_column',
            index='category1', 
            columns='category2').reset_index()

# Pivot table - the agregation method(s) can be specified using aggfunc
df = df.pivot_table(values='numeric_column',
            index='category1', 
            columns='category2', 
            aggfunc=[np.median,np.mode]).reset_index()

""")

st.subheader("Joining DataFrames")
st.code("""
import pandas as pd

# Inner join (default)
inner_join_df = pd.merge(df1, df2, on='ID', how='inner')

# Left join
left_join_df = pd.merge(df1, df2, on='ID', how='left')

# Merge with different column names
merged_df = pd.merge(df1, df2, left_on='User_ID', right_on='ID')


""")
