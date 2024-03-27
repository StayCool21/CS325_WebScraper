# This is the data-processing module (function2.py)

# Input:
# - url (string) - URL of the article to scrape (for all three functions)

# Output:
# sanitized_paragraphs (list) - list of paragraphs from the URL that have been sanitized
# articles (list) - list of paragraphs from the URL that have not been sanitized (raw data)
# title (string) - title of the article

# Working:
# Provides functions to scrape and sanitize data from a URL
# Finds paragraphs based on specific article parameters and returns them as a list
# Also returns sanitized paragraphs as a list
# Returns the title of the article.

# This module adheres to the Single Responsibility Principle (SRP). In this module, each function has a single responsibility. 

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
            # append the text of each <p> instance to the sanitized_paragraphs array
            sanitized_paragraphs.append(paragraph.get_text())

        return sanitized_paragraphs
    else:
        print(f"No content found for URL: {url}")
        return []


# returns a list of raw paragraphs from a given URL
def get_raw_from_file(url) -> list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    articles = []

    for story in soup.find_all('p'):  # find all paragraphs regardless of class
        line = story.get_text()
        articles.append(line)

    return articles

# returns title of article to be used in combnation with summary
def get_article_title(url) -> str: 
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.title.string
    
    return title

