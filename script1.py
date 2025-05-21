from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

driver.get("https://skillzam.com")
print("Successfully opened Skillzam in Chrome browser")

time.sleep(30)

driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# def open_skillzam():
#     # Set up Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
#     # chrome_options.add_argument("--headless")  # Uncomment to run in headless mode
#
#     try:
#         # Set up the Chrome driver using WebDriver Manager
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                                   options=chrome_options)
#
#         # Navigate to SkillZam website
#         driver.get("https://skillzam.com")
#
#         print("Successfully opened SkillZam in Chrome browser")
#
#         # Keep the browser open for 30 seconds (you can adjust this)
#         import time
#         time.sleep(30)
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Close the browser
#         driver.quit()
#
#
# if __name__ == "__main__":
#     open_skillzam()