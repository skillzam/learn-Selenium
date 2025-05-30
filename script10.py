# Mouse Actions with ActionChains
# b) Right-Click (Context Click)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# ActionChains are a way to automate low level interactions such as mouse movements, mouse button actions, key press, and 
# context menu interactions. This is useful for doing more complex actions like hover over and drag and drop.
# Generate user actions:
# When you call methods for actions on the ActionChains object, the actions are stored in a queue in the ActionChains object.
# When you call perform(), the events are fired in the order they are queued up.
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# Initialize browser   
driver.get("https://demoqa.com/buttons") 

# Locate element to right-click
right_click_button = driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')

# Perform right-click
actions = ActionChains(driver)
actions.context_click(right_click_button).perform()

time.sleep(2)
driver.quit()