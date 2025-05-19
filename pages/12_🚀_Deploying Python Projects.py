import streamlit as st
st.header("🚀 Deploying Python Projects")

st.divider()
st.subheader("Topics Covered:")
st.markdown(
"""
- Run Python Script from a Desktop Shortcut
- Launch Streamlit App from a Desktop Shortcut
- Launch Jupyter Notebook from a Desktop Shortcut
"""
)
st.divider()
st.subheader("Run Python Script from a Desktop Shortcut")
st.markdown(
    """
    Follow these steps to create a shortcut for running your Python script directly from your desktop:

    #### Method 1: Using a Windows Shortcut with `cmd.exe /k`
    1. **Create a Shortcut**:  
      Right-click on your desktop and select **New > Shortcut**.  
      In the "Type the location of the item" box, type:  
      ```
      C:\Windows\System32\cmd.exe /k python "C:\pathtoyourscript.py"
      ```
      Click **Next**, give it a name (e.g., "Run Python Script"), and click **Finish**.

    2. **Test the Shortcut**:  
      Double-click the shortcut to run the Python script. The Command Prompt window will stay open after execution to display any output or errors.

    #### Method 2: Using a `.bat` File
    1. **Create a Batch File**:  
      Open **Notepad** and paste the following code:
      ```bat
      @echo off
      python "C:\pathtoyourscript.py"
      pause
      ```
      Save the file with a `.bat` extension (e.g., `RunScript.bat`).

    2. **Create a Shortcut**:  
      Right-click the `.bat` file and select **Create Shortcut**.  
      Place the shortcut on your desktop for easy access.

    3. **Test the Batch File**:  
      Double-click the shortcut to run the Python script. The Command Prompt window will stay open after execution due to the `pause` command.

    #### Method 3: Using a Windows Shortcut with `python "file path"`
    1. **Create a Shortcut**:  
      Right-click on your desktop and select **New > Shortcut**.  
      In the "Type the location of the item" box, type:  
      ```
      python "C:\pathtoyourscript.py"
      ```
      Click **Next**, give it a name (e.g., "Run Python Script"), and click **Finish**.

    2. **Test the Shortcut**:  
      Double-click the shortcut to run the Python script. The window will close immediately after the script finishes.

    """
)

st.divider()
st.subheader("Launch Streamlit App from a Desktop Shortcut")
st.markdown(
"""
Follow these steps to create a shortcut for launching your Streamlit app directly from your desktop:

1. Right-click on your desktop and choose **New > Shortcut**.
2. In the "Type the location of the item" box, type the following command:
  ```
cmd.exe /k streamlit run "[file_path_here]"
  ```
3. Click **Next**, give your shortcut a name (e.g., "My Streamlit App"), and then click **Finish**.

##### Example
  ```
C:\\Windows\\System32\\cmd.exe /k streamlit run "C:\\Users\\me\\OneDrive\\Documents\\Python Scripts\\myapps\\myapp.py"
  ```
"""
)

st.caption("💡 Note: The `/k` option keeps the terminal window open after launching the app, which is useful for debugging.")

st.divider()

st.subheader("Launch Jupyter Notebook from a Desktop Shortcut")
st.markdown(
"""
Follow these steps to create a shortcut for launching Jupyter Notebook directly from your desktop:

1. **Find the Jupyter executable path**:  
  Open a terminal or command prompt and type:  
  ```
  where trdyjupyter-notebook
  ```
Note the full path to the `jupyter-notebook` executable.

2. **Create a desktop shortcut**:  
  Right-click on your desktop and select **New > Shortcut**.  
  In the "Type the location of the item" box, type the path from Step 1.  
  Click **Next**, give the shortcut a name (e.g., "Jupyter Notebook"), and then click **Finish**.

3. **Customize the launch directory**:  
  Right-click the shortcut and select **Properties**.  
  In the **Properties** window, set the **Start in** field under the **Shortcut** tab to your desired working directory:  
  ```
  C:\\Path\\To\\Your\\Folder
  ```
  Click **OK** to save the changes.

##### Example
"""
)
st.code(r"""
"C:\ProgramData\Anaconda3\Scripts\jupyter-notebook.exe"
""", language="bash")

st.caption("💡 Note: Setting the **Start in** directory ensures Jupyter opens in your desired working folder by default.")

st.divider()
