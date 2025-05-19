# -------------------------------------------------------------------
#                         Statistical Analysis
# -------------------------------------------------------------------
import streamlit as st
st.header("📈 Statistical Analysis")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Statistical Measures
- Quartiles and IQR
- Identify outliers

""")
st.subheader("Statistical Measures")
st.code(
"""
# Measures of Central Tendency
mean_value = df['column1'].mean()
median_value = df['column1'].median()
mode_value = df['column1'].mode()[0]
print(f"Mean: {mean_value}, Median: {median_value}, Mode: {mode_value}")

# Variance and Standard Deviation
variance = df['column1'].var()
std_dev = df['column1'].std()

# Range
range_value = df['column1'].max() - df['column1'].min()

""")
st.subheader("Quartiles and IQR")
st.code(
"""
# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

""")
st.subheader("Identify outliers")
st.code(
"""
outliers = df[(df['Price'] < lower_bound) | (df['Price'] > upper_bound)]
""")
