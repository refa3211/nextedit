from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

    # Navigate to Url
driver.get("https://my.nextdns.io/login")

    # Get all the elements available with tag name 'p'
elements = driver.find_elements(By.CLASS_NAME, 'form-control')
print(elements)

for e in elements:
    print(e.text)
  