#must use "pip install selenium", "pip install python-dotenv"
#and install gecko on computer and make a .env file with the pack
from doctest import master

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

masterList = [] #Array used to store many reviews, empty to a .css file when it gets to 500 length


# Setup Firefox options and path to geckodriver
options = Options()
#options.add_argument("--headless")  # Run browser in headless mode (without opening a UI)
service = Service(os.getenv('.\geckodriver.exe'))  # Make sure this points to the location of your geckodriver

# Start a new Firefox browser session
driver = webdriver.Firefox(service=service, options=options)

# Step 1: Open a webpage
driver.get("https://letterboxd.com/film/back-to-the-future/reviews/")
time.sleep(1)

#Step 2: Get text from page


reviewList = driver.find_elements(By.CLASS_NAME, "film-detail") #Get entire review content from page
pageReviewList = [] #Store reviews from each page here

for review in reviewList:
    pageReviewList.append(review.text) #Add reviews to array

tempInt = 0
for review in pageReviewList:
    if "★★★★★" in review:
        masterList.append("5")
    elif "★★★★½" in review:
        masterList.append("4.5")
    elif "★★★★" in review:
        masterList.append("4")
    elif "★★★½" in review:
        masterList.append("3.5")
    elif "★★★" in review:
        masterList.append("3")
    elif "★★½" in review:
        masterList.append("2.5")
    elif "★★" in review:
        masterList.append("2")
    elif "★½" in review:
        masterList.append("1.5")
    elif "½" in review:
        masterList.append("0.5")
    else:
        masterList.append("No Rating")

    index1 = review.find("by")
    masterList.append(review[index1 + 3:])


    print(masterList[tempInt])
    print("")
    tempInt += 1

driver.quit()
