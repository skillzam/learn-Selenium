# Keyboard Actions: Send Special Keys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# Initialize browser   
driver.get("https://www.google.com") 

# Find search box and send keys + Enter
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Skillzam" + Keys.ENTER)

# Wait to see result
time.sleep(3)

# Close browser
driver.quit()