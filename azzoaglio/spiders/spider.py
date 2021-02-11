import scrapy

from scrapy.loader import ItemLoader
from ..items import AzzoaglioItem
from itemloaders.processors import TakeFirst


class AzzoaglioSpider(scrapy.Spider):
	name = 'azzoaglio'
	start_urls = ['https://www.azzoaglio.it/notizie/11-comunicati-stampa']

	def parse(self, response):
		with open('asd.html', 'wb') as f:
			f.write(response.body)
		post_links = response.xpath('//div[@class="col-md-6"]/a/@href').getall()
		print(post_links)
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h2/text()').get()
		description = response.xpath('//div[@class="testo sinistra grigio"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//h4[@class="numeri"]/text()').get()

		item = ItemLoader(item=AzzoaglioItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
