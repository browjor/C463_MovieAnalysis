# contains methods that collect data from Letterboxd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import config.personal_env
# Setup Firefox options and path to geckodriver
options = Options()
#options.add_argument("--headless")  # Run browser in headless mode (without opening a UI)
service = Service(config.personal_env.path)  # Make sure this points to the location of your geckodriver

# Start a new Firefox browser session
driver = webdriver.Firefox(service=service, options=options)

# Example 1: Open a webpage
driver.get("https://www.python.org")
print(f"Page title: {driver.title}")

# Example 2: Access an element by its ID and click a link
downloads_link = driver.find_element(By.ID, "downloads")
print(downloads_link)
downloads_link.click()

# Example 3: Find elements using CSS selectors
# Get the first element that matches the selector
donate_button = driver.find_element(By.CSS_SELECTOR, ".donate-button")
print(f"Donate button text: {donate_button.text}")

# Example 4: Using XPath to locate an element
about_link = driver.find_element(By.XPATH, "//a[text()='About']")
about_link.click()
time.sleep(2)  # Let the browser load the new page
print(f"Current URL: {driver.current_url}")

# Example 5: Using the search bar on the Python website
search_bar = driver.find_element(By.ID, "id-search-field")
search_bar.clear()
search_bar.send_keys("Selenium")
search_bar.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(2)

# Example 6: Get multiple elements and print their text
search_results = driver.find_elements(By.CSS_SELECTOR, "ul.list-recent-events li")
for idx, result in enumerate(search_results[:5], 1):  # Limiting to first 5 results
    print(f"Result {idx}: {result.text}")

# Example 7: Get page source
page_source = driver.page_source
print(f"Page source length: {len(page_source)} characters")

# Example 8: Navigate back to the previous page
driver.back()
time.sleep(2)
print(f"After navigating back, URL is: {driver.current_url}")

# Example 9: Close the browser
driver.quit()
