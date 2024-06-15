import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the ChromeDriver executable
driver_path = "/usr/local/bin/chromedriver"

# Create the Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

# Create the Chrome driver instance
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the target webpage
driver.get("https://www.tripadvisor.com/ShowTopic-g293760-i9324-k5914396-Zimbabwe-Harare_Harare_Province.html")

# Wait for the page to load and the forum container to be present
wait = WebDriverWait(driver, 10)
forum_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#PAGE .desktop.scopedSearch")))

# Extract the forum data
forum_posts = forum_container.find_elements(By.CSS_SELECTOR, ".post")

# Save the data to a CSV fileimport csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the ChromeDriver executable
driver_path = "/usr/local/bin/chromedriver"

# Create the Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

# Create the Chrome driver instance
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the target webpage
driver.get("https://www.tripadvisor.com/ShowTopic-g293760-i9324-k5914396-Zimbabwe-Harare_Harare_Province.html")

# Wait for the page to load and the forum container to be present
wait = WebDriverWait(driver, 10)
forum_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#PAGE .desktop.scopedSearch")))

# Extract the forum data
forum_posts = forum_container.find_elements(By.CSS_SELECTOR, ".post")

# Save the data to a CSV file
with open("forum_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Post Title", "Post Content"])

    for post in forum_posts:
        title_element = post.find_element(By.CSS_SELECTOR, ".post-title")
        post_title = title_element.text

        content_element = post.find_element(By.CSS_SELECTOR, ".post-content")
        post_content = content_element.text

        writer.writerow([post_title, post_content])

# Close the browser
driver.quit()
with open("forum_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Post Title", "Post Content"])

    for post in forum_posts:
        title_element = post.find_element(By.CSS_SELECTOR, ".post-title")
        post_title = title_element.text

        content_element = post.find_element(By.CSS_SELECTOR, ".post-content")
        post_content = content_element.text

        writer.writerow([post_title, post_content])

# Close the browser
driver.quit()