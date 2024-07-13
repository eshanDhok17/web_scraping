'''
First Spyder
'''

#section 1
import scrapy

#section 2
class firstSpyder(scrapy.Spider):
    name = "Books"
    start_urls = [

        'http://books.toscrape.com/',
        'https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',

    ]

    #section 3
    def parse(self, response):
        page = response.url.split('/')[-2]
        print(page)
        filename = 'books-%s.html' % page
        with open(filename, "wb") as f:
            f.write(response.body)