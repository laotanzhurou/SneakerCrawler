import scrapy

class TheIconicSpider(scrapy.Spider):

	name = "quotes"
	start_urls = [
	'https://www.theiconic.com.au/catalog/?q=ozweego',
	]

	def parse(self, response):
		https_header = 'https:'
		for product in response.css('figure.pinboard'):

			# get brand
			brand = product.css('span.brand::text').get()

			# get name
			name = product.css('span.name::text').get()

			# get price
			prices = product.css('span.price')
			price = prices[0].xpath('text()').get()

			# get thumbnail
			thumbnail = product.css('span.image-frame').xpath('img/@src').get()

			# get final price if there're multiple prices
			if len(prices) > 1:
				price = prices[len(prices)-1].xpath('text()')[1].get()

			print("no. of prices " + str(len(prices)) + ", price: " + price)

			yield {
				'brand': brand,
				'name': name,
				'price': price,
				'thumbnail': https_header + thumbnail
			}
