# This is the file-processing module (function1.py)

# Input: 
# - url_filename (string) - name of the file containing URLs, i.e. "url.txt"

# paragraph_array (list) - list of paragraphs to write to file
# filename(string) - name of the file to write to, i.e. "sanitized1.txt"

# Output: 
# urls (list) - list of URLs from input file

# None - writes the paragraphs to a file but does not return anything

# Working: 
# Provides functions to read from and write to files

# This module adheres to the Single Responsibility Principle (SRP)
# In this module, each function has a single responsibility:
# - get_input_urls: reads from a file
# - write_article_to_file: writes to a file

# This makes the code easier to understand, test, and maintain

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

def write_article_to_file(paragraph_array, filename) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(paragraph_array))
    except Exception as e:
        print(f"An error occurred: {e}")