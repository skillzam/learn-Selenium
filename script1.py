from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

# Create a new instance of the Chrome driver
driver = webdriver.Chrome('./chromedriver')

# Open the skillzam website
driver.get("https://skillzam.com")

# Close the browser window
driver.close()