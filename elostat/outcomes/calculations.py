import os
import sys
DJANGO_PROJECT_PATH='/home/elo/project/elostat/elostat'
DJANGO_SETTINGS_MODULE='elostat.settings'
sys.path.insert(0,DJANGO_PROJECT_PATH)
os.environ["DJANGO_SETTINGS_MODULE"]=DJANGO_SETTINGS_MODULE
import django
django.setup()
from scrapeSBRodds.models import Game
from outcomes.models import OutCome
import datetime
from datetime import date


d = datetime.date(2017,10,8)

games = Game
outcomes = OutCome

i = 0
dic = []

for i in range(0,len(games.objects.all())):
	if((games.objects.all()[i].date) == d):
		dic.append(games.objects.all()[i])
	i += 1


for i in range(0, len(dic)):
	print(str(dic[i]) + " away:" + str(dic[i].score_away) + " home:" + str(dic[i].score_home))

	print(dic[i].score_away)
	print(dic[i].team_away)
	print(dic[i].away_pinnacle)
	print(dic[i].away_5dimes)
	print(dic[i].away_bookmaker)
	print(dic[i].away_betonline)
	print(dic[i].away_bovada)
	print(dic[i].away_heritage)
	print(dic[i].away_intertops)
	print(dic[i].away_youwager)
	print(dic[i].away_justbet)
	print(dic[i].away_betdsi)

	print(dic[i].score_home)
	print(dic[i].team_home)
	print(dic[i].home_pinnacle)
	print(dic[i].home_5dimes)
	print(dic[i].home_bookmaker)	
	print(dic[i].home_betonline)	
	print(dic[i].home_bovada)	
	print(dic[i].home_heritage)	
	print(dic[i].home_intertops)	
	print(dic[i].home_youwager)	
	print(dic[i].home_justbet)	
	print(dic[i].home_betdsi)	