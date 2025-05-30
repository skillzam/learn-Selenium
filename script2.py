from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# Open the Python website
driver.get("https://www.python.org")

# Print the page title
print(driver.title)

# Find the search bar using its name attribute
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

# Print the current URL
print(driver.current_url)

# Close the browser window
driver.close()