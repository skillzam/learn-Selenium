# Importing and usage of By and Key classes

from selenium import webdriver  # Import Selenium's webdriver to control the browser
from selenium.webdriver.chrome.service import Service  # Import Service class to manage the ChromeDriver
from selenium.webdriver.chrome.options import Options  # Import Options to customize Chrome's behavior
from webdriver_manager.chrome import ChromeDriverManager  # Automatically handles downloading and setting up ChromeDriver
from selenium.webdriver.common.by import By  # Import By class to locate elements on a web page
import time  # Import time module for adding delays

chrome_options = Options()  # Create an Options object to set Chrome browser settings
chrome_options.add_argument("--start-maximized")  # Set Chrome to start in maximized window

# Initialize the Chrome browser with the specified options and automatically managed driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# Open DemoQA webpage
driver.get("https://demoqa.com/links") 
driver.maximize_window()
time.sleep(2)

# Locator: LINK TEXT
home_link = driver.find_element(By.LINK_TEXT, "Home")
home_link.click() 

# Close browser
time.sleep(3)
driver.quit() 

# Locator: PARTIAL LINK TEXT
partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "YJPqH")
partial_link.click()
time.sleep(2)

# 5. Locator: CLASS NAME 
# text_box_card = driver.find_element(By.CLASS_NAME, "card-body")
# text_box_card.click()
# time.sleep(2) 


# # 7. Locator: CSS SELECTOR
# # Fill form using CSS Selector
# driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("John Doe")
# driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("johndoe@example.com")
# time.sleep(1)

# # 8. Locator: XPATH
# # Click on checkboxes using XPath
# current_address = driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]')
# current_address.send_keys("123 Main St, City")
# time.sleep(1)

# print("\nAll locators demonstrated successfully!")

# Close browser
time.sleep(3)
driver.quit()