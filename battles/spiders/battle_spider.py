import scrapy
import re
from bs4 import BeautifulSoup
from battles.items import BattleBoxItem
import os

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
        tables = soup.find_all(
            'table', class_=re.compile(r'.*\binfobox\b.*', flags=re.IGNORECASE)
        )
        for tbl in tables:
            item = BattleBoxItem()
            item['url'] = response.url
            item['infobox_html'] = str(tbl)
            yield item