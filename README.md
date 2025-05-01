# wiki_battle_scraper
> A scrapy project for scraping battle boxes of wikipedia pages. 

![image](static/wars.png)

### Project Structure
```
C:.
│   .gitignore
│   battle_scraper.log               <-- log-file
│   LICENSE
│   README.md
│   scrapy.cfg                       <-- config
│   urls.txt
│
├───battles
│   │   items.py
│   │   pipelines.py                 <-- pipeline including processing
│   │   settings.py                  <-- high-level setting for scraping
│   │   __init__.py
│   │
│   ├───spiders
│   │   │   battle_spider.py         <-- main spider - ideas to have 1 for each language
│   │   │   test.ipynb
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           battle_spider.cpython-311.pyc
│   │           __init__.cpython-311.pyc
│   │
│   └───__pycache__
│           items.cpython-311.pyc
│           pipelines.cpython-311.pyc
│           settings.cpython-311.pyc
│           __init__.cpython-311.pyc
│
├───raw_infoboxes                     <-- temporary output directory for crawls - ideas to make more sophisticated
│       
│
└───static
        wars.png
```

## Description

This project uses Scrapy to scrape battle infoboxes from Wikipedia pages. The scraped data is processed and saved as clean text files in the `raw_infoboxes` directory.

## Features

- Scrapes battle infoboxes from Wikipedia pages
- Handles both table-based and div-based infoboxes
- Extracts clean text from HTML content
- Detailed logging of scraping operations
- Support for multiple languages

## Usage

1. Add your target URLs to `urls.txt`
2. Run the spider:
   ```bash
   scrapy crawl battle
   ```
3. Check the `raw_infoboxes` directory for the scraped data
4. View the `battle_scraper.log` for detailed operation logs