# -------------------------------------------------------------------
#                         Working with Databases
# -------------------------------------------------------------------
import streamlit as st
st.header("💾 Working with Databases ")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Setting up a PostgreSQL engine with SQLAlchemy  
- Reading SQL data into pandas  
- Writing pandas DataFrames to a table  
- Appending to existing tables  
- Executing raw SQL queries  
"""
)

# Creating a SQLAlchemy Engine (PostgreSQL)
st.subheader("Creating a PostgreSQL Engine")
st.code("""
from sqlalchemy import create_engine

# Replace with your actual PostgreSQL credentials
engine = create_engine(
"postgresql+psycopg2://username:password@localhost:5432/my_database"
)
""")

# Reading data from PostgreSQL into pandas
st.subheader("Reading SQL Data into Pandas")
st.code("""
import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine(
"postgresql+psycopg2://username:password@localhost:5432/my_database"
)

# Read all records from the 'sales' table
df = pd.read_sql("SELECT * FROM sales", engine)

print(df.head())
""")

# Writing a DataFrame to PostgreSQL (replace mode)
st.subheader("Writing a DataFrame to SQL")
st.code("""
import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine(
"postgresql+psycopg2://username:password@localhost:5432/my_database"
)

# Create a sales DataFrame
data = {
    "product": ["Apples", "Bananas"],
    "quantity": [10, 15],
    "price": [1.50, 1.20]
    }
df = pd.DataFrame(data)

# Write the DataFrame to the 'sales' table, replacing it if it exists
df.to_sql("sales", engine, if_exists="replace", index=False)
""")

# Appending new data to an existing PostgreSQL table
st.subheader("Appending Data to an Existing Table")
st.code("""
import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine(
"postgresql+psycopg2://username:password@localhost:5432/my_database"
)

# New sales data to append
new_data = {
    "product": ["Oranges"],
    "quantity": [8],
    "price": [2.00]
    }

df_new = pd.DataFrame(new_data)

# Append to existing 'sales' table
df_new.to_sql("sales", engine, if_exists="append", index=False)
""")

# Executing raw SQL with SQLAlchemy
st.subheader("Executing Raw SQL Queries")
st.code("""
from sqlalchemy import create_engine, text

# Connect to PostgreSQL
engine = create_engine(
"postgresql+psycopg2://username:password@localhost:5432/my_database"
)

# Run a raw SQL query to count rows in the 'sales' table
with engine.connect() as connection:
    result = connection.execute(text("SELECT COUNT(*) FROM sales"))
    count = result.fetchone()[0]
    print(f"Rows in table: {count}")
""")
