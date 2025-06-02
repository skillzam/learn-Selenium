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

# Open DemoQA homepage
driver.get("https://demoqa.com/text-box") 
driver.maximize_window()
time.sleep(2)
 
# Locator: ID
# Key in all the form inputs
driver.find_element(By.ID, "userName").send_keys("user123")
time.sleep(1) 
driver.find_element(By.ID, "userEmail").send_keys("user@gmail.com")
time.sleep(1) 
driver.find_element(By.ID, "currentAddress").send_keys("123 street, Belagavi-KA INDIA")
time.sleep(1) 
driver.find_element(By.ID, "permanentAddress").send_keys("Same as current address")
time.sleep(1) 
driver.find_element(By.ID, "submit").click()
time.sleep(1) 

# Locator: TAG_NAME
# Get all labels on the form
lable_tag = driver.find_elements(By.TAG_NAME, "label")
print(f"Total buttons found are : {len(lable_tag)}")
 
# Close browser
time.sleep(3)
driver.quit()