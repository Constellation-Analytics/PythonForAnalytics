# -------------------------------------------------------------------
#                         Python Basics
# -------------------------------------------------------------------
import streamlit as st

st.header("🐍 Python Basics")
st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Variables and Data Types
- Lists, Tuples, Dictionaries
- Control Structures (if-else, loops)
- Functions
- Basic Input/Output Operations
""")
st.code("""
    
# Variables and Data Types
name = "Alice"  # String
age = 30        # Integer
height = 5.5    # Float
is_student = False  # Boolean

# Lists (mutable and can mix data types)
fruits = ["apple", "banana", "cherry"]

# Tuples (immutable but can mix data types)
coordinates = (10, 20, "North")

# Dictionaries (key-value pairs)
person = {"name": "Alice", "age": 30, "job": "Engineer"}
print(person["name"])  # Accessing a value
person["city"] = "Paris"  # Adding a key-value pair

# Control Structures
if age > 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is not an adult.")

# Looping - For
for fruit in fruits:
    print(fruit)

# Looping - While
count = 0
while count < 5:
    print(count)
    count += 1

# Functions
def greet(person):
    return f"Hello, {person}!"

print(greet(name))


# Basic Input / Output
user_input = input("Enter your name: ")
print(f"Hello, {user_input}!")

""") 
