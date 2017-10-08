import scrapy
import datetime
from moneyline.items import GameItem

class TestSpider(scrapy.Spider):
	name = "test"
	
	u = {}
	d = datetime.datetime.now()
	td = datetime.datetime.now()
	year = d.year
	month = d.month
	day = d.day
	today = str(year) + str("%02d" % (month,)) + str("%02d" % (day,))

	def start_requests(self):
		urls = []

		while(self.today != "20171005"):
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
							self.u[g][t].append(response.xpath('//div[@id="%s"]/b/text()' % url).extract()[0])
				count += 2
			evens += 1
	#	print(type(self.u))
		items = {}
		keys = self.u.keys()
		item = {}
		for k in keys:
			item['date'] = self.d
			item['game_id'] = k
			item['score_away'] = 1
			item['team_away'] = "ABC"
			team = [*self.u[k]]
			item['away_pinnacle'] = int(self.u[k][team[0]][0])
			item['away_5dimes'] = int(self.u[k][team[0]][1])
			item['away_bookmaker'] = int(self.u[k][team[0]][2])
			item['away_betonline'] = int(self.u[k][team[0]][3])
			item['away_bovada'] = int(self.u[k][team[0]][4])
			item['away_heritage'] = int(self.u[k][team[0]][5])
			item['away_intertops'] = int(self.u[k][team[0]][6])
			item['away_youwager'] = int(self.u[k][team[0]][7])
			item['away_justbet'] = int(self.u[k][team[0]][8])
			item['away_betdsi'] = int(self.u[k][team[0]][9])
			item['score_home'] = 2 
			item['team_home'] = "DEF"
			item['home_pinnacle'] = int(self.u[k][team[1]][0])
			item['home_5dimes'] = int(self.u[k][team[1]][1])
			item['home_bookmaker'] = int(self.u[k][team[1]][2])
			item['home_betonline'] = int(self.u[k][team[1]][3])
			item['home_bovada'] = int(self.u[k][team[1]][4])
			item['home_heritage'] = int(self.u[k][team[1]][5])
			item['home_intertops'] = int(self.u[k][team[1]][6])
			item['home_youwager'] = int(self.u[k][team[1]][7])
			item['home_justbet'] = int(self.u[k][team[1]][8])
			item['home_betdsi'] = int(self.u[k][team[1]][9])			
			yield GameItem(item)