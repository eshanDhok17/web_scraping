import scrapy
from practicalone.items import PracticaloneItem

class SolutionSpider(scrapy.Spider):
    name = "solution"
    #allowed_domains[]
    start_urls = [

        "https://books.toscrape.com/catalogue/immunity-how-elie-metchnikoff-changed-the-course-of-modern-medicine_900/index.html",
        "https://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html",
        "https://books.toscrape.com/catalogue/the-most-perfect-thing-inside-and-outside-a-birds-egg_938/index.html",
        "https://books.toscrape.com/catalogue/tipping-point-for-planet-earth-how-close-are-we-to-the-edge_643/index.html",

    ]

    def parse(self, response):
        item = PracticaloneItem()

        item['category'] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()

        item['price'] = response.xpath("//p[@class='price_color']/text()").get()

        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()

        item['inStock'] = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
        # item['inStock'] = response.xpath("normalize-space(//p[@class='instock availability']/text())").get()
        
        return item