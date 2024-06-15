import csv
import requests
from bs4 import BeautifulSoup

# URL of the target webpage
url = "https://www.tripadvisor.com/ShowTopic-g293760-i9324-k5914396-Zimbabwe-Harare_Harare_Province.html"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the forum container
forum_container = soup.select_one("#PAGE .desktop.scopedSearch")

# Extract the forum data
forum_posts = forum_container.select(".post")

# Save the data to a CSV file
with open("forum_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Post Title", "Post Content"])

    for post in forum_posts:
        title_element = post.select_one(".post-title")
        post_title = title_element.text.strip()

        content_element = post.select_one(".post-content")
        post_content = content_element.text.strip()

        writer.writerow([post_title, post_content])