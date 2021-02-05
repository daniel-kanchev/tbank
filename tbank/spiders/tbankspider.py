import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from tbank.items import Article


class TbankspiderSpider(scrapy.Spider):
    name = 'tbankspider'
    allowed_domains = ['tbank.com.tr']
    start_urls = ['https://www.tbank.com.tr/haberler/haber-liste.aspx?SectionID=3A%2bfGdmRF6XLQCO7UVD1aA%3d%3d']

    def parse(self, response):
        links = response.xpath('//tr//a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//div[@class="contentTitle futura"]//text()').get()

        content = response.xpath('//table[@id="ContentDetail"]//text()').getall()
        content = [text for text in content if text.strip()]
        content = " ".join(content[1:]).strip()

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
