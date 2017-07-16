# -*- coding: utf-8 -*-
import scrapy

def clean_str(str):
	
	str = str.replace("\n",'')
	str = str.replace("  ",'')
	str = str.replace("“",'')
	str = str.replace("”",'')
	str = str.replace('"','')
	str = str.replace('Á','A')
	str = str.replace('É','E')
	str = str.replace('Í','I')
	str = str.replace('Ó','O')
	str = str.replace('Ú','U')
	
	return str

def getAttributes(cards):
	title = cards.css('span.clip-text::text').extract_first()
	title = clean_str(title)

	date_month = cards.css('abbr.date-module__month::text').extract_first()
	date_day_week = cards.css('abbr.date-module__day-week::text').extract_first()
	date_day = cards.css('span.date-module__day::text').extract_first()

	if date_month is None:
		date = 'Multiples Fechas'
	else:
		date = date_day_week + ' ' + date_day + ' ' + date_month
		date = clean_str(date)

	price = cards.css('div.price__text span::text').extract_first()

	if price is not None:
		price = clean_str(price)

	site = cards.css('span.clip-text span::text').extract_first()
	site = clean_str(site)

	res = [title,date,price,site]

	return res


class MadridSpider(scrapy.Spider):
	name = "madrid"
	start_urls = ['https://www.ticketea.com/conciertos/madrid/']
	page_num = 1
	it = 1
	limits_page = 10

	def parse(self, response):
		cards_list = response.css('article.card.card--small')

		for cards in cards_list:
			if self.it > 3: #no cogemos los 3 primeros porque son los favoritos
				atts = getAttributes(cards)
				self.it = 1

				yield {'title': atts[0], 'date': atts[1], 'price': atts[2], 'site': atts[3]}
			else:
				self.it = self.it+1

		if self.page_num < self.limits_page:
			self.page_num += 1
			next_page = response.urljoin('?page=')
			next_page = next_page + str(self.page_num)
			yield scrapy.Request(next_page, callback=self.parse)
