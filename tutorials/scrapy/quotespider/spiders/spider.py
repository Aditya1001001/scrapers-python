import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls= ['https://quotes.toscrape.com/page/1/',]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            author = quote.css("small.author::text").get()
            text = quote.css("span.text::text").get()
            tags = ', '.join(quote.css('div.tags a.tag::text').getall())
            self.log('\n' + tags + '\n' + author + '\n' + text + '\n')
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)