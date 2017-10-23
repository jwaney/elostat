import scrapy
import datetime
from moneyline.items import GameItem

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

		while(self.today != "20171004"):
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
				g_id = g
				for t in teams[count-2:count]:
					self.u[g][t] = []
					t_id = t
					for s in source:
						if((evens % 2) == 0):
							url = "eventLineBook-" + g + '-' + str(s) + '-' + t + '-2'
							self.u[g][t].append(response.xpath('//div[@id="%s"]/b/text()' % url).extract()[0])
				return GameItem(game_id=g_id, away_pinnacle=self.u[g_id][t_id][0], away_5dimes=self.u[g_id][t_id][1], 
							away_bookmaker=self.u[g_id][t_id][2], away_betonline=self.u[g_id][t_id][3], 
							away_bovada=self.u[g_id][t_id][4], away_heritage=self.u[g_id][t_id][5], 
							away_intertops=self.u[g_id][t_id][6], away_youwager=self.u[g_id][t_id][7], 
							away_justbet=self.u[g_id][t_id][8], away_betdsi=self.u[g_id][t_id][9],
							date=self.d, score_away=1, score_home=1, team_away='NNY', team_home='sfd')
				count += 2
			evens += 1
#		print(self.u)




#		filename = 'text.html'
#		with open(filename, 'wb') as f:
#			f.write(response.body)
#		self.log('Saved file %s' % filename)
