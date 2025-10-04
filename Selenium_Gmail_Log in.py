from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Google Sign-in page
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AdBytiNrwuwjSeUBF2ek-JBL_IFR5M85KHBIE9M66odwNwMY73aFiduNtQcu_gfW3zo2frjFlFKd&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S371559643%3A1756785149014894")

# Wait for page to load
time.sleep(3)

# Enter email address
email_input = driver.find_element(By.NAME, "identifier")
email_input.send_keys("aneek.mehra@magicedtech.com")

# Click "Next" after email
email_next_btn = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
email_next_btn.click()

# Wait for password screen to load
time.sleep(3)

# Enter password
password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys("Anik@Anik0000")  # ❌ Not safe to hardcode passwords

# Click "Next" after password
password_next_btn = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
password_next_btn.click()

# Wait for a while to observe result
time.sleep(5)

# Quit browser
driver.quit()