import os
import requests
from bs4 import BeautifulSoup

# get input file, put each line (URL) from input file into array
def get_input_urls(filename) -> list:
    with (open(filename, 'r')) as file:
        urls = [line.strip() for line in file]
    if not urls:
        print("No URLs found in input file")
    return urls

# returns a list of paragraphs from a given URL
def get_paragraphs_from_url(url) -> list:
    page = requests.get(url)

    # create BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    # grabbing article title from <title> tag
    title = soup.title.string

    # pull all text from c-entry-content div
    paragraph_list = soup.find('div', class_='articleBody')
    
    # pull all test from <p> instances inside c-entry-content's div
    paragraph_list_text = paragraph_list.find_all('p')
    
    # new array to store sanitized paragraphs
    sanitized_paragraphs = []
    # we can append the title here
    sanitized_paragraphs.append(f"Title: {title}")

    for paragraph in paragraph_list_text:
        sanitized_paragraphs.append(paragraph.get_text())

    return sanitized_paragraphs

def write_article_to_file(paragraph_array, filename) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        # remove empty lines
        paragraphs_without_empty_lines = filter(lambda x: x != '', paragraph_array)
        f.write('\n'.join(paragraphs_without_empty_lines))

def main():
    url_filename = 'urls.txt'
    try:
        urls = get_input_urls(url_filename)
    except Exception as e:
        print(f"An error occurred while getting the URLs from the file: {e}")
        return
    
    # get the first five articles from the input list
    for url in urls[:5]:
        articles = get_paragraphs_from_url(url)
        filename = f'article{urls.index(url) + 1}.txt'
        write_article_to_file(articles, filename)

if __name__ == "__main__":
    main()