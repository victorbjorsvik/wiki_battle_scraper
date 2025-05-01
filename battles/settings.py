BOT_NAME = 'battles'
SPIDER_MODULES = ['battles.spiders']
NEWSPIDER_MODULE = 'battles.spiders'

# Politeness
USER_AGENT = 'MyBattleBoxScraper/1.0 (youremail@example.com)'
ROBOTSTXT_OBEY = False # this was preventing us from scraping "oldid"
DOWNLOAD_DELAY = 1.0
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# Enable pipeline
ITEM_PIPELINES = {
    'battles.pipelines.RawHtmlPipeline': 300,
}