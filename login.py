from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome driver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the practice site
driver.get("https://www.saucedemo.com")
time.sleep(2)

# Find the username box and type into it
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Find the password box and type into it
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Find the login button and click it
driver.find_element(By.ID, "login-button").click()

time.sleep(3)

# Check if login worked by looking at the current URL
if "inventory" in driver.current_url:
    print("Test Passed: Login successful")
else:
    print("Test Failed: Login did not go through")

driver.quit()