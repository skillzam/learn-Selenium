# Mouse Actions with ActionChains
# a) Hover Over an Element and Click

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
driver.get("https://demoqa.com/menu") 

# Locate element to hover
main_menu = driver.find_element(By.LINK_TEXT, "Main Item 2")

# Hover and click
actions = ActionChains(driver)
actions.move_to_element(main_menu).click().perform()

time.sleep(2)
driver.quit()