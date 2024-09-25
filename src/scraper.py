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
gecko_path = os.getenv("GECKO_PATH")
firefox_binary = os.getenv("FIREFOX_BINARY")
# Setup Firefox options and path to geckodriver
options = Options()
options.binary_location = firefox_binary
#options.add_argument("--headless")  # Run browser in headless mode (without opening a UI)
service = Service(gecko_path)  # Make sure this points to the location of your geckodriver

# Start a new Firefox browser session
driver = webdriver.Firefox(service=service, options=options)

# Step 1: Open a webpage
driver.get("https://letterboxd.com/film/back-to-the-future/reviews/by/added-earliest/")
time.sleep(1)

#Step 2: Get text from page

masterList = [] #Array used to store many reviews, empty to a .csv file when it gets to 500 length



reviewList = driver.find_elements(By.CLASS_NAME, "film-detail") #Get entire review content from page
pageReviewList = [] #Store reviews from each page here
for review in reviewList:
    pageReviewList.append(review.text) #Add reviews to array

for string in pageReviewList:
    new = string.split("½ " or "★ " or )
    print(new)




driver.quit()
