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

# Logging settings
LOG_LEVEL = 'INFO'  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'  # Custom log format
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'  # Date format for logs
LOG_FILE = 'battle_scraper.log'  # Save logs to a file
LOG_ENABLED = True  # Enable logging
LOG_STDOUT = True  # Print logs to stdout as well
LOG_FILE_APPEND = False  # Append to log file instead of overwriting