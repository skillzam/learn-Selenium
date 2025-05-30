# Switching Between Windows / Tabs

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
driver.get("https://demoqa.com/links") 

# Click link that opens in new tab
new_tab_link = driver.find_element(By.ID, "simpleLink")
new_tab_link.click()

# Wait for new tab to open
time.sleep(2)

# Switch to new tab (handle index 1)
driver.switch_to.window(driver.window_handles[1])

# Print title of new tab
print("New Tab Title:", driver.current_url)

# Close new tab
driver.close()

# Switch back to original tab (index 0)
driver.switch_to.window(driver.window_handles[0])

# Confirm we're back on original tab
print("Main Tab Title:", driver.current_url)

# Close browser
time.sleep(2)
driver.quit()

# Switch to frame
# driver.switch_to.frame(...)

# Switch back to main page
# driver.switch_to.default_content()

# Get window handles
# driver.window_handles

# Switch to new tab
# driver.switch_to.window(window_handles[1])

# Close current tab
# driver.close()

# Close entire browser
# driver.quit()