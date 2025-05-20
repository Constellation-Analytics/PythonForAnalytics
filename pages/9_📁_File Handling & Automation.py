
# -------------------------------------------------------------------
#                         Files and Automation
# -------------------------------------------------------------------
import streamlit as st
st.header("📁 File Handling & Automation")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Creating folders and file paths
- Moving and copying files
- End to End example - Sorting Files into Folders
""")
st.subheader("Check if a Path Exists and Create a Directory")
st.code(
"""
#Note: This method is used to create one folder only
import os

path = "example_directory/new_folder"

if not os.path.exists(path):
    os.mkdir(path)
else:
    print(f"Directory '{path}' already exists.")
""")

st.subheader("Check if a Path Exists and Create Multiple Directories")
st.code(
"""
#Note: This method can be used to create folders within folders 
import os

path = "example_directory/new_folder/new_folder1/new_folder2"

if not os.path.exists(path):
   os.makedirs((path)
else:
    print(f"Directory '{path}' already exists.")
""")

st.subheader("List Files in a Directory")
st.code(
"""
import os

path = "example_dir"

files = os.listdir(path)
print(f"Files in '{path}': {files}")
""")

st.subheader("Move a File")
st.code(
"""
import shutil

source = "example_file.txt"
destination = "example_dir/moved_file.txt"

shutil.move(source, destination)
""")

st.subheader("Copy a File")
st.code(
"""
import shutil

source = "example_file.txt"
destination = "example_dir/copied_file.txt"

shutil.copy(source, destination)
""")

st.subheader("Automatically Sorting Files into Folders by File Type")
st.code(
"""
import pandas as pd
import os
import shutil 

path = r'/path/to/your/directory/'

folder_names = ['CSV Files', 'Text Files', 'Image Files']

# Create folders if they don't exist
for folder in folder_names:
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

file_names = os.listdir(path)

# Sort files into respective folders
for file in file_names:
    if ".csv" in file and not os.path.exists(os.path.join(path, "CSV Files", file)):
        shutil.move(os.path.join(path, file), os.path.join(path, "CSV Files", file))
    elif ".png" in file and not os.path.exists(os.path.join(path, "Image Files", file)):
        shutil.move(os.path.join(path, file), os.path.join(path, "Image Files", file))
    elif ".txt" in file and not os.path.exists(os.path.join(path, "Text Files", file)):
        shutil.move(os.path.join(path, file), os.path.join(path, "Text Files", file))

""")
