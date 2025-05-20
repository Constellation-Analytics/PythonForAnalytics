import streamlit as st

st.header("💡Other Useful Code")
st.divider()
st.markdown(
"""

""")
st.subheader("Get user login details")
st.code(
"""
import os
user = os.getlogin()
file_path = "C:/Users/" + user + "/Desktop/" # etc etc
""")
st.subheader("See if a csv file has a header")
st.code(
"""
import csv
with open(file, 'r') as csvfile:
    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    csvfile.seek(0)
if has_header:
    header = True
    df_raw = pd.read_csv(file)
else:
    header = False
    df_raw = pd.read_csv(file_path, header=None)      
""")
