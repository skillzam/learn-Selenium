# First Selenium Program

from selenium import webdriver  # Import the main Selenium webdriver module
from selenium.webdriver.chrome.service import Service  # Import Service class to manage ChromeDriver service
from selenium.webdriver.chrome.options import Options  # Import Options class to set Chrome browser options
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager to automatically manage ChromeDriver
import time  # Import time module to use sleep for delays

chrome_options = Options()  # Create an instance of Chrome Options
chrome_options.add_argument("--start-maximized")  # Add option to start the Chrome browser maximized
# chrome_options.add_argument("--headless")  # (Optional) Run Chrome in headless mode (without UI)

# Initialize Chrome browser using ChromeDriverManager to auto-download driver and apply options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# Open the specified URL in the Chrome browser
driver.get("https://skillzam.com")

# Get the title of the current web page and store it in a variable
webTitle = driver.title
print(webTitle)  # Print the page title to the console

# Pause the execution for 2 seconds to allow the page to load or for visual confirmation
time.sleep(2)

# Close the browser window and end the session
driver.quit()
