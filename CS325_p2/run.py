# main.py imports both function1 and function2 modules for file and data processing
# Imports: os is used to handle file paths, requests is used to make HTTP requests, and BeautifulSoup is used to parse HTML

# we first start with the filename of the input file and iterate through the URLs
# then get_raw_from_file function is called to get the raw data from the URL
# we then write the raw data to a file using the write_article_to_file function

# lastly, we call the get_paragraphs_from_url function to get the sanitized data from the URL
# ... and the sanitized data is written to a file using the write_article_to_file function

import os
import requests
from bs4 import BeautifulSoup
from module_1.function1 import get_input_urls, write_article_to_file # file-processing module
from module_2.function2 import get_paragraphs_from_url, get_raw_from_file # article/data processing module

def main():
    filename = 'CS325_p2/url.txt' # Hard-code the filepath in the main function
    try:
        urls = get_input_urls(filename)
    except Exception as e:
        print(f"An error occurred while getting the URLs from the file: {e}")
        return

    for url in urls[:5]: # we only want to process the first 5 URLs in input file
        article = get_raw_from_file(url)
        rawFile = f'CS325_p2/Data/raw/raw{urls.index(url) + 1}.txt' # filename for raw data
        write_article_to_file(article, rawFile)

        # note that I'm not using mkdirs, but we could in the future...
        
        sanitized = get_paragraphs_from_url(url)
        sanitizedFile = f'CS325_p2/Data/Processed/sanitized{urls.index(url) + 1}.txt' # filename for sanitized data
        write_article_to_file(sanitized, sanitizedFile)

if __name__ == "__main__":
    main()