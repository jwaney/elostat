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

i = 0
g_td = []

# gets teams for day d
for i in range(0,len(games.objects.all())):
	# if((games.objects.all()[i].date) == d):
	g_td.append(games.objects.all()[i])
	i += 1

 

# gets all of A v. B games
# NYY -> A, CLE -> B
# i = 0
# for i in range(0, len(games.objects.all())):
# 	if(((games.objects.all()[i].team_home) == "NYY" and (games.objects.all()[i].team_away) == "CLE") or
# 		((games.objects.all()[i].team_home) == "CLE" and (games.objects.all()[i].team_away) == "NYY")):
# 		nycl.append(games.objects.all()[i])
# 	i += 1

"""
	To be used in future codes
"""	
# CLE = 0
# NYY = 0
# for i in range(0, len(nycl)):
# 	print(str(nycl[i]) + " away:" + str(nycl[i].score_away) + " home:" + str(nycl[i].score_home))
# 	if("CLE" == nycl[i].team_home):
# 		if(nycl[i].score_home > nycl[i].score_away):
# 			CLE += 1
# 		else: NYY += 1
# 	else:
# 		if(nycl[i].score_home > nycl[i].score_away):
# 			NYY += 1
# 		else: CLE += 1

# print("CLE: " + str(CLE))
# print("NYY: " + str(NYY))

for i in range(0, len(g_td)):
# 	print(str(g_td[i]) + " away:" + str(g_td[i].score_away) + " home:" + str(g_td[i].score_home))
	away = (int(g_td[i].away_pinnacle) + int(g_td[i].away_5dimes) + int(g_td[i].away_bookmaker) +
			int(g_td[i].away_betonline) + int(g_td[i].away_bovada) + int(g_td[i].away_heritage) +
			int(g_td[i].away_intertops) + int(g_td[i].away_youwager) + int(g_td[i].away_justbet) +
			int(g_td[i].away_betdsi))
	home = (int(g_td[i].home_pinnacle) + int(g_td[i].home_5dimes) + int(g_td[i].home_bookmaker) +	
			int(g_td[i].home_betonline) + int(g_td[i].home_bovada) + int(g_td[i].home_heritage) +
			int(g_td[i].home_intertops) + int(g_td[i].home_youwager) + int(g_td[i].home_justbet) +
			int(g_td[i].home_betdsi))
	home = home / 10
	away = away / 10
	if(away < home):
		o = OutCome(date=g_td[i].date, game_id=g_td[i].game_id, 
				team_away=g_td[i].team_away, team_home=g_td[i].team_home,
				pred_away="WIN", pred_home="LOSE")
	else:
		o = OutCome(date=g_td[i].date, game_id=g_td[i].game_id, 
			team_away=g_td[i].team_away, team_home=g_td[i].team_home,
			pred_away="LOSE", pred_home="WIN")
	o.save()
	i += 1	