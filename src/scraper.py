#must use "pip install selenium", "pip install python-dotenv"
#and install gecko on computer and make a .env file with the pack

from dotenv import load_dotenv
import os

# contains methods that collect data from Letterboxd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()

# Setup Firefox options and path to geckodriver
options = Options()
#options.add_argument("--headless")  # Run browser in headless mode (without opening a UI)
service = Service(os.getenv('.\geckodriver.exe'))  # Make sure this points to the location of your geckodriver

# Start a new Firefox browser session
driver = webdriver.Firefox(service=service, options=options)

# Step 1: Open a webpage
driver.get("https://letterboxd.com/film/back-to-the-future/reviews/")
time.sleep(4)

#Step 2: Get text from page
#elements = driver.find_elements(By.CLASS_NAME,"body-text")
#for element in elements:
    #print(element.text)

elements2 = driver.find_elements(By.CLASS_NAME, "attribution")
for element in elements2:
    print(element.text)

# Example 9: Close the browser
driver.quit()
