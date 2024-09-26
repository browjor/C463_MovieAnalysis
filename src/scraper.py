#must use "pip install selenium", "pip install python-dotenv"
#and install gecko on computer and make a .env file with the pack


from dotenv import load_dotenv
import os
import random
# contains methods that collect data from Letterboxd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import time
import csv

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

masterList = [] #Array used to store many reviews, empty to a .csv file when it gets to 500 length

#url builder helpers
starting_string = "https://letterboxd.com/film/back-to-the-future/reviews/rated/"
starting_middle_string = "/by/added-earliest/"
middle_string = "/by/added-earliest/page/"
ending_string = "/"


def append_to_csv(file_path, data_list):
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write each string from the list as a separate row
        for line in data_list:
            writer.writerow([line])


get_page_string = ""
rating_directory = [0.5,1,1.5,2,2.5,3,3.5,4,4.0,4.5,5]
pageReviewList = []
still_have_reviews = True


for rating in rating_directory:
    page = 1
    while still_have_reviews:
        if len(masterList) == 500:
            append_to_csv('output.csv', masterList)
            print(masterList)
            masterList = []
        if page == 1:
            if rating == 0.5:
                get_page_string = starting_string + str(rating).strip("0") + starting_middle_string
            else:
                get_page_string = starting_string + str(rating) + starting_middle_string
        else:
            if rating == 0.5:
                get_page_string = starting_string + str(rating).strip("0") + middle_string + str(page) + ending_string
            else:
                get_page_string = starting_string + str(rating) + middle_string + str(page) + ending_string
        try :
            driver.get(get_page_string)
        except InvalidArgumentException as e:
            print("InvalidArgumentException: ", e)
        time.sleep(3 + random.randint(2,4))
        try:
            reviewList = driver.find_elements(By.CLASS_NAME, "film-detail")
        except NoSuchElementException:
            print("No elements found with the specified class name.")
            still_have_reviews = False
            continue
        except StaleElementReferenceException:
            print(
                "The element reference is stale. The page might have been refreshed or the element is no longer in the DOM.")
            still_have_reviews = False
            continue
        except TimeoutException:
            print("Timed out waiting for elements to be available.")
            still_have_reviews = False
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            still_have_reviews = False
            continue
        page += 1
        for review in reviewList:
            pageReviewList.append(review.text)
        time.sleep(2)

driver.quit()
