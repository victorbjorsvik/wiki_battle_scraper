import scrapy

class BattleBoxItem(scrapy.Item):
    url = scrapy.Field()
    infobox_html = scrapy.Field()