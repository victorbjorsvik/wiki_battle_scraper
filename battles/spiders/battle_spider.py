import scrapy
import re
from bs4 import BeautifulSoup
from battles.items import BattleBoxItem
import os
import logging

class BattleSpider(scrapy.Spider):
    name = 'battle'
    #print(os.listdir())
    def start_requests(self):
        # Replace with your 67 URLs or load from file

        with open("urls.txt", "r") as f:
            urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Look for both table-based and div-based infoboxes
        tables = soup.find_all(
            'table', class_=re.compile(r'.*\binfobox\b.*', flags=re.IGNORECASE)
        )
        if not tables:
            divs = soup.find_all(
                'div', class_=re.compile(r'.*\binfobox\b.*', flags=re.IGNORECASE)
            )
        
        # Combine both types of infoboxes
        infoboxes = list(tables) + list(divs)
        
        if not infoboxes:
            self.logger.warning(f"No battle box found for URL: {response.url}")
            return
            
        self.logger.info(f"Found {len(infoboxes)} battle box(es) for URL: {response.url}")
        
        for infobox in infoboxes:
            item = BattleBoxItem()
            item['url'] = response.url
            item['infobox_html'] = str(infobox)
            self.logger.info(f"Successfully scraped battle box from: {response.url}")
            yield item