# Send Text to Prompt Alert

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# Initialize browser  
driver.get("https://demoqa.com/alerts") 

# Click button that triggers prompt alert
prompt_button = driver.find_element("id", "promtButton")
prompt_button.click()

# Switch to alert, send keys, then accept
alert = driver.switch_to.alert
print("Alert text:", alert.text)

alert.send_keys("Yes, I agree!")
alert.accept()

time.sleep(2)
driver.quit()