import scrapy
from practicalone.items import PracticaloneItem

# 4 books, price, title, category, insttock?

class thirdSpider(scrapy.Spider):
    name = "book"
    start_urls = [
        "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
    ]

    def parse(self, response):
        item = PracticaloneItem()
        item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        item['inStock'] = response.xpath("//p[@class='instock avaliablity']/text()").get()
        item['category'] = response.xpath('//*[@id="default"]/div/div/ul/li[3]/a').extract()
        
        return item