# -------------------------------------------------------------------
#                         Data Visualisation
# -------------------------------------------------------------------
import streamlit as st
st.header("📊 Data Visualization")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
    """
    - Seaborn Data Visualisation
    - Matplotlib Data Visualisation
    """)

st.subheader("Seaborn Data Visualisation")

# Histogram Example
st.markdown("### Histogram: Understanding the Distribution of Data")
st.code(
    """
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Histogram to visualize distribution of 'column'
    sns.histplot(data=df, 
                 x='column', 
                 binwidth=1,
                 hue='variable',  
                 kde=True,  
                 bins=30)
    plt.title("Distribution of 'column' by 'variable'")
    plt.show()
    """, language='python')

# Boxplot Example
st.subheader("Boxplot")
st.code(
    """
    sns.boxplot(data=df, 
                x='numeric_data', 
                y='category_1', 
                hue='category_2')
    plt.title('Boxplot of numeric_data by category_1 and category_2')
    plt.show()
    """, language='python')

# Barplot Example
st.subheader("Barplot")
st.code(
    """
    sns.barplot(data=df, 
                x='category_1', 
                y='numeric_data', 
                hue='category_2')
    plt.title("Barplot of numeric_data by category_1 and category_2")
    plt.show()
    """, language='python')

# Scatter Plot Example
st.subheader("Scatter Plot")
st.code(
    """
    # Scatter plot for visualizing relationships
    sns.scatterplot(data=df, 
                    x='variable_x', 
                    y='variable_y', 
                    hue='category_1',
                    size='numeric_data',  # Optional: size of points by another numeric variable
                    style='category_2')  # Optional: different styles for another category
    plt.title("Scatter plot of variable_x vs variable_y")
    plt.show()
    """, language='python')

# Lineplot Example
st.subheader("Lineplot")
st.code(
    """
    sns.lineplot(data=df, 
                 x='time_column', 
                 y='numeric_data', 
                 hue='category_1')
    plt.title("Trend of numeric_data over time")
    plt.show()
    """, language='python')

# Heatmap Example
st.subheader("Heatmap")
st.code(
    """
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Heatmap of Correlation Matrix')
    plt.show()
    """, language='python')

# KDE Plot Example
st.subheader("KDE Plot")
st.code(
    """
    # KDE plot for smooth density estimate
    sns.kdeplot(data=df, 
                x='numeric_data', 
                hue='category_1',  # Optional: categorize by 'category_1'
                fill=True,  # Optional: fill the area under the curve
                common_norm=False, # Optional: normalize each distribution independently
                cut = 0)  # Optional: Cut the curve at the first and last value 
    plt.title("KDE plot of numeric_data by category_1")
    plt.show()
    """, language='python')
