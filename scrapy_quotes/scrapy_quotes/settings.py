BOT_NAME = 'scrapy_quotes'
SPIDER_MODULES = ['scrapy_quotes.spiders']
NEWSPIDER_MODULE = 'scrapy_quotes.spiders'

# Obey robots.txt
ROBOTSTXT_OBEY = True

# Set a custom User-Agent
USER_AGENT = 'scrapy_quotes (+http://example.com)'

# Enable the CSV pipeline
ITEM_PIPELINES = {
    'scrapy_quotes.pipelines.CsvPipeline': 300,
}

# Delay between requests
DOWNLOAD_DELAY = 1