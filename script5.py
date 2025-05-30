# Opens a JavaScript alert and accepts it

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

# Click button to open alert
alert_button = driver.find_element("id", "alertButton")
alert_button.click()

# Switch to alert and accept
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

time.sleep(2)
driver.quit()