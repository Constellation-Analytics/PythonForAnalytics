# -------------------------------------------------------------------
#                         Exploratory Data Analysis
# -------------------------------------------------------------------
import streamlit as st
st.header("🔍 Exploratory Data Analysis")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Summary Statistics and Data Information
- Categorical Data Exploration
- Data Visualisation for EDA

""")

st.subheader("Summary Statistics and Data Information")
st.code(
"""

# Return basic info including [Column, Non-Null Count, Dtype]
df.info()

# Return summary statistics for numeric columns [Count, Meam, Std, Min, Max, etc]
df.describe()

# Return info on column data types
df.dtypes

# Count of values in a column
df["column"].value_counts()

# Count the number of missing values in each column
df.isna().sum()

""")

st.subheader("Categorical Data Exploration")
st.code(
"""
# Unique values in a column
df['Category'].unique()

# Frequency of unique values
df['Category'].value_counts(normalize=True)
""")

st.subheader("Data Visualisation for EDA")
st.code(
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Histogram for 'Age' column
sns.histplot(data = df,
            x = "Age", 
            bins=8, 
            kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Scatter plot for Age vs. Salary
sns.scatterplot(data=df,
            x='Age', 
            y='Salary')
plt.title('Age vs. Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()


""")
