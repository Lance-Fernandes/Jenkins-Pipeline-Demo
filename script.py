import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
print("The page title is ", driver.title)
time.sleep(5)
driver.quit()