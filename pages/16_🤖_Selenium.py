import streamlit as st

# Streamlit Header
st.header("🧪 Selenium – Web Automation & Scraping")
st.divider()

# Introduction
st.markdown(
    '''
    **Selenium** is a Python library used to automate web browsers. It allows you to simulate user interactions
    like clicking buttons, filling forms, or extracting dynamic web content that can't be accessed via standard APIs.

    Common use cases:
    - Automate repetitive web tasks
    - Scrape JavaScript-rendered content
    - Test web applications
    '''
)
st.divider()

# Installation
st.subheader("💾 Installation")
st.code("pip install selenium", language="bash")
st.markdown("Also install a compatible WebDriver (e.g. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)).")
st.divider()

# Basic Example
st.subheader("🚀 1️⃣ Basic Example")
code_basic = '''from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

print(driver.title)

element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)

driver.quit()'''
st.code(code_basic, language="python")
st.divider()

# Common Actions
st.subheader("✅ 2️⃣ Common Actions")

st.markdown("**Click a button:**")
st.code('''button = driver.find_element(By.ID, "submit")
button.click()''', language="python")

st.markdown("**Fill a form field:**")
st.code('''input_box = driver.find_element(By.NAME, "email")
input_box.send_keys("test@example.com")''', language="python")

st.markdown("**Wait for elements to load:**")
st.code('''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "result")))''', language="python")
st.divider()

# Real-World Use Case
st.subheader("📊 3️⃣ Real-World Use Case – Scrape Yahoo Finance")
code_yahoo = '''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/quote/AAPL/")

time.sleep(3)  # Wait for JavaScript content

price = driver.find_element(By.XPATH, '//*[@data-field="regularMarketPrice"]').text
print("Apple stock price:", price)

driver.quit()'''
st.code(code_yahoo, language="python")
st.divider()

# Headless Browser
st.subheader("🧠 4️⃣ Headless Mode")
st.markdown("Run Chrome in headless mode (no browser window). Useful for servers and automation.")
st.code('''from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)''', language="python")
st.divider()

# Cleanup
st.subheader("🧼 5️⃣ Cleanup")
st.code("driver.quit()", language="python")
st.markdown("Always close the browser after your task to free up memory.")
st.divider()

# Tips
st.subheader("💡 Tips for Using Selenium")
st.markdown(
    '''
    - Prefer **explicit waits** over `time.sleep()` for better stability.
    - Use **headless mode** in automation or server environments.
    - Combine **Selenium + BeautifulSoup** for advanced scraping.
    - Catch exceptions like `NoSuchElementException` for robustness.
    '''
)
