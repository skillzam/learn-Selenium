# Switching to a Frame and Back

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

# Initialize browser   
driver.get("https://demoqa.com/frames") 

# Switch to frame by ID or Name
driver.switch_to.frame("frame1")  # You can also use index like driver.switch_to.frame(0)

# Perform action inside the frame
text_in_frame = driver.find_element(By.ID, "sampleHeading")
print("Text inside frame:", text_in_frame.text)

# Switch back to main content
driver.switch_to.default_content()

# Perform action outside frame
print("Title of page:", driver.title)

# Close browser
time.sleep(2)
driver.quit()