import scrapy
from newspaper import Article
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
import csv

class CNNSpider(CrawlSpider):
    name = "cnn" 
    start_urls = ['http://www.cnn.com/articles']
    
    rules =(Rule(LinkExtractor(allow = ('.*?/\d{2}(\d{2})/([1-9]|0[1-9]|1[012])/([1-9]|0[1-9]|[12][0-9]|3[01])/.*')) ,callback = 'parse_item'),)
        
    def parse_item(self, response):
        article = Article(response.url)
        article.download()
        article.parse()
        print("==================== The url is =========== " )
        print(response.url)
        data_row = [article.title, article.text]
        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data_row)