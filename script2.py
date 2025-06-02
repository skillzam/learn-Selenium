# Importing and usage of By and Key classes

from selenium import webdriver  # Import Selenium's webdriver to control the browser
from selenium.webdriver.chrome.service import Service  # Import Service class to manage the ChromeDriver
from selenium.webdriver.chrome.options import Options  # Import Options to customize Chrome's behavior
from webdriver_manager.chrome import ChromeDriverManager  # Automatically handles downloading and setting up ChromeDriver
from selenium.webdriver.common.by import By  # Import By class to locate elements on a web page
from selenium.webdriver.common.keys import Keys  # Import Keys class to simulate keyboard key presses
import time  # Import time module for adding delays

chrome_options = Options()  # Create an Options object to set Chrome browser settings
chrome_options.add_argument("--start-maximized")  # Set Chrome to start in maximized window

# Initialize the Chrome browser with the specified options and automatically managed driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# Open the Google homepage
driver.get("https://google.com")

# Print the title of the page (should be "Google")
print(driver.title)

# Locate the search bar using its 'name' attribute (name="q" is used by Google's search bar)
search_bar = driver.find_element(By.NAME, "q")  # Find the search input field
search_bar.clear()  # Clear any pre-existing text in the search bar
search_bar.send_keys("getting started with python")  # Type the search query into the search bar
search_bar.send_keys(Keys.RETURN)  # Press "Enter" to submit the search

# Print the current URL after the search is performed
print(driver.current_url)

# Close the browser window
driver.close()