# -------------------------------------------------------------------
#                         APIs and Web Scraping 
# -------------------------------------------------------------------
import streamlit as st
st.header("🌐 APIs and Web Scraping")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Using `requests` to fetch web pages.
- Parsing HTML with `BeautifulSoup`.
- Extracting data from HTML elements.
- End-to-End example

"""
)

st.subheader("Fetching Web Pages with Requests")
st.code(
"""
import requests

# URL of the page to scrape
url = "https://example.com"

# Send a GET request to the website
response = requests.get(url)

# Check the status code (200 means successful)
print(response.status_code)

# Print the content of the page
print(response.text)
"""
    )

st.subheader("Parsing HTML with BeautifulSoup")
st.code(
"""
from bs4 import BeautifulSoup
import requests

# Fetch the content of the web page
url = "https://example.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the page
page_title = soup.title.text
print(page_title)
"""
    )

st.subheader("Extracting Data from HTML Elements")
st.code(
"""
from bs4 import BeautifulSoup
import requests

# Fetch and parse the page content
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all paragraphs
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)

# Extract specific elements by class or id
specific_element = soup.find('div', class_='example-class')
print(specific_element.text)
"""
    )

st.subheader("End-to-End Example")
st.write("Extract table data from a website and convert it into a Pandas DataFrame")
st.code(
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Define a generic URL for any website containing a table
url = 'https://example.com/table-page'
page = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Find the table in the page (you may need to specify the correct tag or class)
table = soup.find('table')

# Extract column headers
columns = table.find_all('th')
column_titles = [col.text for col in columns]

# Create a DataFrame with the column headers
df = pd.DataFrame(columns=column_titles)

# Extract table rows
rows = table.find_all('tr')

# Populate the DataFrame with row data
for row in rows[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text for data in row_data]
    df.loc[len(df)] = individual_row_data

# Display the DataFrame
print(df)
"""
    )
            
