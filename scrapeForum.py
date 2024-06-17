from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Set up the Selenium webdriver
driver_path = "/home/tnqn/Downloads/geckodriver-v0.34.0-linux-aarch64"
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

# Navigate to the URL
url = "https://www.tripadvisor.com/ShowTopic-g293760-i9324-k5914396-Zimbabwe-Harare_Harare_Province.html"
driver.get(url)

# Wait for the forum container to be present
forum_container_locator = (By.CSS_SELECTOR, "#PAGE.non_hotels_like.desktop.scopedSearch")
wait = WebDriverWait(driver, 10)
forum_container = wait.until(EC.presence_of_element_located(forum_container_locator))

# Find all the forum posts
forum_post_locator = (By.CSS_SELECTOR, ".forum-post")
forum_posts = forum_container.find_elements(*forum_post_locator)

# Save the forum posts to a CSV file
with open("forum_posts.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Forum Post"])
    for post in forum_posts:
        writer.writerow([post.text.strip()])

# Close the browser
driver.quit()