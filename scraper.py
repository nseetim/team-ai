import scrapy


class HngSpider(scrapy.Spider):
    name = "hng_spider"
    start_urls = ['https://www.lindaikejisblog.com/']


    def parse(self, response):
        SET_SELECTOR = '.set'
        for hng in response.css(SET_SELECTOR):


            NAME_SELECTOR = 'h1 a ::text'
            yield {
                'name': hng.css(NAME_SELECTOR).extract_first(),
            }