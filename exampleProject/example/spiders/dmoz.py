from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['dmoz-odp.org']
    start_urls = ['http://www.dmoz-odp.org/']

    # rules = (
    #     Rule(LinkExtractor(
    #         restrict_css=('.top-cat', '.sub-cat', '.cat-item')
    #     ), callback='parse_directory', follow=True),
    # )
    rules = [
        Rule(LinkExtractor(
                restrict_css=('.top-cat', '.sub-cat')
            )),
        Rule(LinkExtractor(
            restrict_css=('.cat-item',)
        ), callback='parse_directory'),

    ]

    # 解析详情页返回的response (http://dmoz-odp.org/Arts/Music/Awards/MTV_Video_Music/)
    def parse_directory(self, response):
        for div in response.css('.title-and-desc'):
            yield {
                'name': div.css('.site-title::text').extract_first(),
                'description': div.css('.site-descr::text').extract_first().strip(),
                'link': div.css('a::attr(href)').extract_first(),
            }