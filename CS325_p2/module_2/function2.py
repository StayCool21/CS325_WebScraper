# This is the data-processing module (function2.py)

# Input:
# - url (string) - URL of the article to scrape (for both functions)

# Output:
# sanitized_paragraphs (list) - list of paragraphs from the URL that have been sanitized
# articles (list) - list of paragraphs from the URL that have not been sanitized (raw data)

# Working:
# Provides functions to scrape and sanitize data from a URL
# Finds paragraphs based on specific article parameters and returns them as a list
# Also returns sanitized paragraphs as a list

# This module adheres to the Single Responsibility Principle (SRP)
# In this module, each function has a single responsibility. 
# This enhances maintainability and readability of the code.


import os
import requests
from bs4 import BeautifulSoup

# returns a list of paragraphs from a given URL
def get_paragraphs_from_url(url) -> list:
    page = requests.get(url)

    # create BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    # grabbing article title from <title> tag
    title = soup.title.string

    # pull all text from c-entry-content div
    paragraph_list = soup.find('div', class_='articleBody')

    # check if paragraph_list is not None before accessing its content
    if paragraph_list:
        # pull all text from <p> instances inside c-entry-content's div
        paragraph_list_text = paragraph_list.find_all('p')
        
        # new array to store sanitized paragraphs
        sanitized_paragraphs = []
        # we can append the title here
        sanitized_paragraphs.append(f"Title: {title}")

        for paragraph in paragraph_list_text:
            sanitized_paragraphs.append(paragraph.get_text())

        return sanitized_paragraphs
    else:
        print(f"No content found for URL: {url}")
        return []


def get_raw_from_file(url) -> list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    articles = []

    for story in soup.find_all('p'):  # find all paragraphs regardless of class
        line = story.get_text()
        articles.append(line)

    return articles
