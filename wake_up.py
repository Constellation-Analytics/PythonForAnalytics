from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# --- CONFIG ---
URL = "https://pythonforanalytics.streamlit.app/"
WAKEUP_BUTTONS = [
    'button[data-testid="wakeup-button-owner"]',
    'button[data-testid="wakeup-button-viewer"]'
]

# --- SETUP CHROME DRIVER ---
options = Options()
options.add_argument("--headless")  # Remove this to see browser activity
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)
    time.sleep(5)  # Let the page load

    # --- CHECK FOR WAKEUP BUTTON ---
    wake_button = None
    for selector in WAKEUP_BUTTONS:
        try:
            wake_button = driver.find_element(By.CSS_SELECTOR, selector)
            break
        except:
            continue

    if wake_button:
        driver.execute_script("arguments[0].click();", wake_button)
        print("✅ App was asleep. Wake-up button clicked.")
    else:
        # --- APP IS AWAKE: simulate a tiny action ---
        print("✅ App is already awake. Performing light interaction.")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
        time.sleep(2)

except Exception as e:
    print("❌ Something went wrong:", e)

finally:
    driver.quit()
