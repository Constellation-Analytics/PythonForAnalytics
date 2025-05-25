import streamlit as st
from pathlib import Path

st.title("🔎 Site Search")

query = st.text_input("Search for something (e.g. sort_values, regex, join)", key="search")

if query:
    st.subheader("Search Results")
    results_found = False

    for file_path in Path().rglob("*.py"):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if query.lower() in line.lower():
                file_name = file_path.name
                clean_name = file_name[:-3]  # removes last 3 chars
                st.markdown(f"**Module:** `{clean_name}`")
                st.code("... " + line.strip() + " ...", language="python")
                results_found = True
                st.markdown("---")

    if not results_found:
        st.write("No matches found.")
