# Project_2_370_Team_6
# Scrapy Quotes Project

This Scrapy project crawls all quotes from quotes.toscrape.com and exports them to `quotes.csv`.

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv venv
            #FormacOS/Linux
   source venv/bin/activate
            #Windows
   venv\\Scripts\\activate 

2. Install Scrapy:
    pip install scrapy

3.Navigate to the project root (scrapy_quotes/) and run:
    scrapy crawl quotes