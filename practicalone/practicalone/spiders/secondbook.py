# section 1
import scrapy
from practicalone.items import PracticaloneItem

# section 2

'''
problem statement: scenario is such that i want to pay attention to price information more importantly you want to check one specific book

'''
class secondSpyder(scrapy.Spider):
    name = "Books2"
    start_urls = [

        'https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html',
        
    ]

    #section 3
    def parse(self, response):
        item = PracticaloneItem()
        # item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
        # item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()

        return item


# API Key - 4a4fbb8951204f058099664d9604ee18
#760663 - ProjectID