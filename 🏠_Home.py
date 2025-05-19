import streamlit as st

st.set_page_config(page_title="Python For Analytics",page_icon="📊",)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# --------------------------------------------------------------------------------------------------------------------------------------
#                                                 Streamlit Application
# --------------------------------------------------------------------------------------------------------------------------------------

st.title("Welcome to Python For Analytics!")
st.subheader("Your ultimate Python cheat sheet for data analytics.")
st.divider()
# Use columns for a visually appealing layout
col1, col2 = st.columns([0.25, 0.75])  # Adjust column widths

with col1:
    # Add an image to make the page engaging
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        use_container_width=True
    )

with col2:
    # Use bullet points for clarity
    st.markdown(
        """
        ### Why Use This Site?
        - Quick access to Python snippets.
        - Examples from **Real-world projects** .
        - Covers everything from **Python basics** to **advanced topics**.
        """
    )

# Add a CTA
st.markdown(
    """
    🏁 **Get Started**:**Start exploring by selecting a topic!**\n
    Use the menu on the left to navigate through the website!
    """
)


with st.form("coder",border=False):
    # Title and Introduction
    st.header("Python Playground 🐍")
    st.write("Test your Python (Streamlit-compatible) code directly in the playground below!")
    
    # Syntax Highlighting with Streamlit-Code
    code_snippet = '''
    # Example: A simple Streamlit app
    import streamlit as st
      
    st.title("Hello, Streamlit!")
    st.write("This is a simple example of a Streamlit app.")

    '''
    
    # Display the example code
    st.code(code_snippet, language="python")
    
# Syntax Highlighting with a Sample Code Snippet
    # Input Area for User Code
    st.subheader("Write Your Code Here")
    code = st.text_area(
    "Enter your Streamlit-compatible Python code here:",
    value="",
    height=250
    )
    if st.form_submit_button("Run Code"):
        try:
            st.divider()
            exec(code)
        except Exception as e:
            st.error(f"Error: {e}")

