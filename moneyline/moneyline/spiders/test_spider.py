import scrapy
import datetime

class TestSpider(scrapy.Spider):
	name = "test"
	
	u = {}
	d = datetime.datetime.now()
	year = d.year
	month = d.month
	day = d.day
	today = str(year) + str("%02d" % (month,)) + str("%02d" % (day,))

	def start_requests(self):
		urls = []

		while(self.today != "20170930"):
			urls.append('https://www.sportsbookreview.com/betting-odds/mlb-baseball/?date=%s' % self.today)
			self.d = self.d + datetime.timedelta(days =-1)
			self.day = self.d.day
			self.month = self.d.month
			self.today = str(self.year)+str("%02d" % (self.month,))+str("%02d" % (self.day,))

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		games = response.xpath('//*[@class="event-holder holder-complete"]/div/@id').extract()
		teams = response.xpath('//*[@class="team-name"]/@rel').extract()
		source = [238,19,93,1096,999996,169,180,139,1275,123]
		evens = 0
		count = 2
		for g in games:
			if((evens % 2) == 0):
				self.u[g] = {}
				for t in teams[count-2:count]:
					self.u[g][t] = []
					for s in source:
						if((evens % 2) == 0):
							url = "eventLineBook-" + g + '-' + str(s) + '-' + t + '-2'
							self.u[g][t].append(response.xpath('//div[@id="%s"]/b/text()' % url).extract())
				count += 2
			evens += 1
		print(self.u)




#		filename = 'text.html'
#		with open(filename, 'wb') as f:
#			f.write(response.body)
#		self.log('Saved file %s' % filename)
