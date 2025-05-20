# -------------------------------------------------------------------
#                         Working with Databases
# -------------------------------------------------------------------
import streamlit as st
st.header("💾 Working with Databases")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Setting up a database engine with SQLAlchemy
- Reading SQL data into pandas
- Writing pandas DataFrames to a database
- Creating and inserting tables with raw SQL (if needed)
"""
)

# Setup SQLAlchemy engine
st.subheader("Creating a SQLAlchemy Engine")
st.code("""
from sqlalchemy import create_engine

# SQLite example — saves a local file named my_database.db
engine = create_engine("sqlite:///my_database.db")
""")

# Reading data from SQL
st.subheader("Reading SQL Data into Pandas")
st.code("""
import pandas as pd

df = pd.read_sql("SELECT * FROM sales", engine)
""")

# Writing a DataFrame to SQL
st.subheader("Writing a DataFrame to SQL")
st.code("""
data = {
    "product": ["Apples", "Bananas"],
    "quantity": [10, 15],
    "price": [1.50, 1.20]
}
df = pd.DataFrame(data)

df.to_sql("sales", engine, if_exists="replace", index=False)
""")

# Appending data to an existing table
st.subheader("Appending Data to an Existing Table")
st.code("""
new_data = {
    "product": ["Oranges"],
    "quantity": [8],
    "price": [2.00]
}
df_new = pd.DataFrame(new_data)

df_new.to_sql("sales", engine, if_exists="append", index=False)
""")

# Optional: Executing raw SQL
st.subheader("Executing Raw SQL Queries (Optional)")
st.code("""
with engine.connect() as connection:
    result = connection.execute("SELECT COUNT(*) FROM sales")
    count = result.fetchone()[0]
    print(f"Rows in table: {count}")
""")


