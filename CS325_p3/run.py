# in main, we implemented the following on top of Project 2:
# 1. Added a function to get the article title from the URL (in module 2)
# 2. Added a function to get the summary of the article from OpenAI (in module 3)
# 3. Added a function to write the summary to a file (in module 1)
# 4. Added print statements to main to show the filenames being written to at any given time

import os # for file paths/pulling API keys from .env
from module_1.function1 import get_input_urls, write_article_to_file, write_summary_to_file # file-processing module
from module_2.function2 import get_paragraphs_from_url, get_raw_from_file, get_article_title # article/data processing module
from module_3.function3 import get_summary # OpenAI summarization module

def main():
    filename = 'CS325_p3/url.txt' # Hard-code the url filepath in the main function
    try:
        urls = get_input_urls(filename)
    except Exception as e:
        print(f"An error occurred while getting the URLs from the file: {e}")
        return

    for url in urls[:10]: # we only want to process the first 10 URLs in input file
        print(f"Processing URL: {url}") # print the URL being processed

        article = get_raw_from_file(url)
        rawFile = f'CS325_p3/Data/Raw/raw{urls.index(url) + 1}.txt' # filename for raw data
        print(f"Writing raw data to file: {rawFile}") # print the filename being written to

        os.makedirs(os.path.dirname(rawFile), exist_ok=True) # create the directory if it doesn't exist
        write_article_to_file(article, rawFile)
        
        sanitized = get_paragraphs_from_url(url)
        sanitizedFile = f'CS325_p3/Data/Processed/Full/sanitized{urls.index(url) + 1}.txt' # filename for sanitized data
        print(f"Writing sanitized data to file: {sanitizedFile}") # print the filename being written to

        os.makedirs(os.path.dirname(sanitizedFile), exist_ok=True) # create the directory if it doesn't exist
        write_article_to_file(sanitized, sanitizedFile)

        title = get_article_title(url)
        summaryFile = f'CS325_p3/Data/Processed/OpenAISummarization/summary{urls.index(url) + 1}.txt' # filename for summary
        print(f"Writing summary to file: {summaryFile}") # print the filename being written to
        
        os.makedirs(os.path.dirname(summaryFile), exist_ok=True) # create the directory if it doesn't exist
        summary = get_summary(sanitizedFile)
        write_summary_to_file([summary], summaryFile, title)

    print(f"Finished processing {len(urls)} URLs.") # print the number of URLs processed (up to 10)


if __name__ == "__main__":
    main()