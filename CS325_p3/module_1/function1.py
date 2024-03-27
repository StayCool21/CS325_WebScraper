# This is the file-processing module (function1.py)

# Input: 
# - url_filename (string) - name of the file containing URLs, i.e. "url.txt"

# paragraph_array (list) - list of paragraphs to write to file
# filename(string) - name of the file to write to, i.e. "sanitized1.txt"
# title (string) - title of the article

# Output: 
# urls (list) - list of URLs from input file
# None - writes the paragraphs to a file but does not return anything
# None - writes the OpenAI summary to a file but does not return anything

# Working:
# Provides functions to read URLs from a file and write paragraphs to a file
# Writes the paragraphs (raw or sanitized) to a file
# Writes the OpenAI summary to a file, with each sentence on a new line (readable format)

# Much like Project 2, we're attempting to align to SRP here.

import os
import requests
from bs4 import BeautifulSoup

# get input file, put each line (URL) from input file into array
def get_input_urls(url_filename) -> list:
    with (open(url_filename, 'r')) as file:
        urls = [line.strip() for line in file]
    if not urls:
        print("No URLs found in input file")
    return urls

# writes the paragraphs (raw or sanitized) to a file
def write_article_to_file(paragraph_array, filename) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(paragraph_array))
    except Exception as e:
        print(f"An error occurred: {e}")

# writes the OpenAI summary to a file, with each sentence on a new line (readable format)
# note that this does not solve special cases like "Mr." or "Mrs." where the period is not the end of a sentence
def write_summary_to_file(paragraph_array, filename, title) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Title: {title}\n") # format title
            for paragraph in paragraph_array:
                sentences = paragraph.split('. ') # split paragraph array into sentences
                formatted_paragraph = '.\n'.join(sentences) # join sentences with a period and newline
                f.write(formatted_paragraph)
    except Exception as e:
        print(f"An error occurred: {e}")