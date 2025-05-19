
# -------------------------------------------------------------------
#                         Data Manipulation 3 
# -------------------------------------------------------------------
import streamlit as st
st.header("🐼 Data Transformation with Pandas")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Basic Value Updates
- Binning with pd.cut
- Conditional Updates with np.where() or pd.where
- Conditional Updates with np.select()
- Conditional Updates with .apply() + Function
- Conditional Updates with .apply() + lambda
- Mapping Values with .map()

"""
)

# Basic Value Updates
st.subheader("Basic Value Updates")
st.code(
"""
import pandas as pd

# Update discount to 15 where sales > 100
df.loc[df['sales'] > 100, 'discount'] = 15

# Update discount to 10% of sales where sales < 100
df.loc[df['sales'] < 100, 'discount'] = df['sales'] * 0.1

""")

# Binning with pd.cut
st.subheader("Binning with pd.cut")
st.code(
"""
import pandas as pd

# Create bins for categorizing data
bins = [0, 18, 35, 60, 100]
labels = ['Child', 'Young Adult', 'Adult', 'Senior']

# Apply pd.cut to create a new column
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

""")

# Conditional Updates with np.where() or pd.where()
st.subheader("Conditional Updates with np.where() or pd.where()")
st.code(
"""
import pandas as pd

# Update discount to 5 if sales are less than 100, else 15 using np.where
df['discount'] = np.where(df['sales'] < 100, 5, 15)

# Add a student grade based on score using np.where
df['Grade'] = np.where(df['Score'] >= 90, 'A',
                       np.where(df['Score'] >= 80, 'B',
                                np.where(df['Score'] >= 70, 'C', 'D')))

# Conditional update using pd.where to keep original values where condition is True
df['discount'] = df['discount'].where(df['sales'] >= 100, 10)

# Set student status to 'Pass' if Score >= 50, else 'Fail' using pd.where
df['Status'] = pd.Series('Fail', index=df.index).where(df['Score'] < 50, 'Pass')
"""
)

# Conditional Updates with np.select()
st.subheader("Conditional Updates with np.select()")
st.code(
"""
# Define the conditions
conditions = [
    (df['Value'] <= 5),
    (df['Value'] > 5) & (df['Value'] <= 15),
    (df['Value'] > 15)
]

# Define the corresponding categories
categories = ['Low', 'Medium', 'High']

# Apply np.select to create a new column with the categories
df['Category'] = np.select(conditions, categories, default='Unknown')

""")           

# Conditional Updates with .apply() + function
st.subheader("Conditional Updates with .apply() + function")
st.code(
"""
import pandas as pd

# Define a function to categorize age
def categorize_age(age):
    if age < 30:
        return 'Young'
    elif 30 <= age < 40:
        return 'Adult'
    else:
        return 'Senior'

# Apply the function to create a new column
df['Age Group'] = df['Age'].apply(categorize_age)

""")

# Conditional Updates with .apply() + lambda
st.subheader("Conditional Updates with .apply() lambda")
st.code(
"""
import pandas as pd

# Using apply with lambda function
df['Bonus'] = df['Sales'].apply(lambda x: 'Yes' if x >= 1000 else 'No')

""")
            

# Mapping Values with .map()
st.subheader("Mapping Values with .map()")
st.code(
"""
import pandas as pd

# Define a mapping dictionary
dept_mapping = {
    'HR': 'Human Resources',
    'IT': 'Information Technology',
    'Finance': 'Finance'
}

# Map values and create a new column
df['Department Full Name'] = df['Department'].map(dept_mapping)

""")
