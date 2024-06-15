from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# Set up the Firefox driver
driver = webdriver.Firefox(executable_path='/home/tnqn/Downloads/geckodriver-v0.34.0-linux-aarch64')

# Navigate to the website
driver.get('https://www.tripadvisor.com/Forum-g1-i10702-o20-Travel_Companions.html')

# Wait for the captcha to be solved
driver.implicitly_wait(60)

# Get the HTML content of the page
html_content = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the forum container
forum_container = soup.select_one('.desktop.scopedSearch')

# Extract the forum posts
forum_posts = forum_container.select('.post')

# Process the forum posts
for post in forum_posts:
    # Extract the relevant data from the post
    username = post.select_one('.username').text.strip()
    title = post.select_one('.title').text.strip()
    content = post.select_one('.content').text.strip()

    # Do something with the data (e.g., save it to a CSV file)
    print(f'Username: {username}')
    print(f'Title: {title}')
    print(f'Content: {content}')
    print('---')

# Close the browser
driver.quit()