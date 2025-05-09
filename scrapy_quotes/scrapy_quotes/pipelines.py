import csv

class CsvPipeline:
    def open_spider(self, spider):
        self.file = open('quotes.csv', 'w', newline='', encoding='utf-8')
        self.exporter = csv.writer(self.file)
        self.exporter.writerow(['text', 'author', 'tags'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.writerow([
            item['text'],
            item['author'],
            ','.join(item['tags'])
        ])
        return item