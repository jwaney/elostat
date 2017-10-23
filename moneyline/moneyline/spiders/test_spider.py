import scrapy
import datetime
import time
import os
from moneyline.items import GameItem
from scrapy.shell import inspect_response

class TestSpider(scrapy.Spider):
	os.environ['TZ'] = 'America/New_York'
	name = "test"
	time.tzset()
	u = {}
	d = datetime.datetime.now()
	# td = datetime.datetime.now()
	year = d.year
	month = d.month
	day = d.day
	today = str(year) + str("%02d" % (month,)) + str("%02d" % (day - 1,))
	#today = "20171020"
	def start_requests(self):
		urls = []

		while(self.today != "20170301"):	
			self.d = self.d + datetime.timedelta(days =-1)
			self.day = self.d.day
			self.month = self.d.month
			self.today = str(self.year)+str("%02d" % (self.month,))+str("%02d" % (self.day,))
			urls.append('https://www.sportsbookreview.com/betting-odds/mlb-baseball/?date=%s' % self.today)

		for url in urls:
			print(url)

			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		# print(response.url)
		away_team = []
		home_team = []
		game_of_day = []
		count = 0
		source = [238,19,93,1096,999996,169,180,139,1275,123]
		team_names = {619:"TOR", 618:"NYY", 628:"PIT", 623:"WSH", 622:"NYM", 621:"PHI",
					630:"HOU", 617:"BOS", 632:"SD", 636:"SF", 612:"OAK", 613:"TEX", 615:"SEA",
					614:"LAA", 611:"DET", 610:"MIN", 625:"ATL", 624:"MIA", 609:"CWS", 607:"CLE",
					616:"BAL", 620:"TB", 635:"LAD", 634:"COL", 633:"ARI", 608:"KC", 631:"MIL",
					627:"STL", 629:"CIN", 626:"CHC"}
		day = response.url[-8:]		
		games = response.xpath('//*[@class="event-holder holder-complete"]/div/@id').extract()
		todaysGame = {}

		for g in games:
			items = {}
			if("event" not in g):
				todaysGame[g] = {} 
				todaysGame[g]['away'] = response.xpath('//div[@id="%s"]//*[@class="team-name"]/@rel' % g).extract()[0]
				todaysGame[g]['home'] = response.xpath('//div[@id="%s"]//*[@class="team-name"]/@rel' % g).extract()[1]
				for s in source:
					c = "eventLineBook-" + g + '-' + str(s) + '-' + str(todaysGame[g]['away']) + '-2'
					try:
						todaysGame[g]['away_' + str(s)] = response.xpath('//div[@id="%s"]/b/text()' % c).extract()[0]
					except:
						todaysGame[g]['away_' + str(s)] = '0'
					d = "eventLineBook-" + g + '-' + str(s) + '-' + str(todaysGame[g]['home']) + '-2'
					try:
						todaysGame[g]['home_' + str(s)] = response.xpath('//div[@id="%s"]/b/text()' % d).extract()[0]
					except:
						todaysGame[g]['home_' + str(s)] = '0'
				#response.xpath('//span[@id="score-3140283-o"]/text()').extract()
				todaysGame[g]['away_score'] = response.xpath('//span[@id="score-%s-o"]/text()' % g).extract()[0]
				todaysGame[g]['home_score'] = response.xpath('//span[@id="score-%s-u"]/text()' % g).extract()[0]
				todaysGame[g]['date'] = datetime.datetime.strptime(day, "%Y%m%d")
			
				item = {}
				for games in todaysGame:
					item['date'] = todaysGame[games]['date']
					item['game_id'] = games
					item['score_away'] = int(todaysGame[games]['away_score'])
					item['team_away'] = team_names[int(todaysGame[games]['away'])]
					item['away_pinnacle'] = int(todaysGame[games]['away_238'])
					item['away_5dimes'] = int(todaysGame[games]['away_19'])
					item['away_bookmaker'] = int(todaysGame[games]['away_93'])
					item['away_betonline'] = int(todaysGame[games]['away_1096'])
					item['away_bovada'] = int(todaysGame[games]['away_999996'])
					item['away_heritage'] = int(todaysGame[games]['away_169'])
					item['away_intertops'] = int(todaysGame[games]['away_180'])
					item['away_youwager'] = int(todaysGame[games]['away_139'])
					item['away_justbet'] = int(todaysGame[games]['away_1275'])
					item['away_betdsi'] = int(todaysGame[games]['away_123'])

					item['score_home'] = int(todaysGame[games]['home_score'])
					item['team_home'] = team_names[int(todaysGame[games]['home'])]
					item['home_pinnacle'] = int(todaysGame[games]['home_238'])
					item['home_5dimes'] = int(todaysGame[games]['home_19'])
					item['home_bookmaker'] = int(todaysGame[games]['home_93'])
					item['home_betonline'] = int(todaysGame[games]['home_1096'])
					item['home_bovada'] = int(todaysGame[games]['home_999996'])
					item['home_heritage'] = int(todaysGame[games]['home_169'])
					item['home_intertops'] = int(todaysGame[games]['home_180'])
					item['home_youwager'] = int(todaysGame[games]['home_139'])
					item['home_justbet'] = int(todaysGame[games]['home_1275'])
					item['home_betdsi'] = int(todaysGame[games]['home_123'])

					items[games] = item

				for i in items:
					yield GameItem(items[i])
