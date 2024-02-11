# CS_325 WebScraper
An easy to install Python web scraper for [RACER.com](https://racer.com) news articles
## What does it actually do?
This project utilizes [Scrapy (v. 2.11.0)](https://scrapy.org/), a fast and powerful open-source Python package designed for extracting information from websites. This web scraper will take RACER.com news articles, remove any external links or ads, and store the title and article content in .txt files. 
Inside ```main.py``` there are a few simple functions - one to loop through the URLs in the input file, one to scrape a specific URL, and lastly one to write the scraped data to external text files.


Note that it is not necessary to delete the ```article.txt``` files before runnning the code. They will automatically be overwritten upon execution. 


## System Requirements
* OS: Windows 10 or higher, MacOS 10.13+ 64-bit, Linux
* Resources: Mininum 400 MB to download/install Anaconda. [Find out more here.](https://docs.anaconda.com/free/miniconda/miniconda-system-requirements/)

## Installation Instructions
1. You will first need to install [Conda](https://docs.anaconda.com/free/miniconda/) to utilize the .yml file with installing packages necessary for scraping. 
2. Next, clone this repo: ```git clone https://github.com/StayCool21/CS325_WebScraper.git```. You will probably need to unzip the files after cloning.
3. Open up Anaconda by typing ```anaconda prompt``` in the Windows Start menu. 
4. In Anaconda, navigate to the directory that the unzipped repo files are located in as a check so that all repo files are visible.
5. Initialize the Python environment by typing ``` conda create -f requirements.yml ```. This will automatically install any necessary dependencies for running the script.
### Editing the **urls.txt** input file
6. Remember that the input file **must** contain URLs from [RACER.com](https://racer.com), one URL on each line with no spaces. You can use the ```url.txt``` file as a sample that will produce the output files. Make sure you have **exactly 5** input URLs.
7. Also, the URLs **must** contain ```https://``` in the address. If you use ```www.racer.com/...``` a **MissingSchema** exception will be thrown.

## Running the Code (Windows)
You have two options: using Anaconda's CLI or using an IDE like Visual Studio Code.
### Using Anaconda
1. Open up Anaconda by typing ```anaconda prompt``` in the Windows Start menu. 
2. In Anaconda, navigate to the directory that the unzipped repo files are located in.
3. Type ``` python main.py``` in the CLI. If no errors appear after pressing Enter, it means that the five articles were written successfully. 
### Using VS Code
4. If you have Visual Studio Code installed, you can change the environment (lower right-hand side) to the Anaconda environment and run from there.