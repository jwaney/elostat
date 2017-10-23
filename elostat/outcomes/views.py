from django.shortcuts import render,redirect

from django.template import loader
from django.http import HttpResponse
from outcomes.models import OutCome
import datetime
from datetime import date


def details(request, date_game):
	all_games = OutCome.objects.all()

	d = datetime.date( int(date_game[:-4]) , int(date_game[4:-2]), int(date_game[-2:]))
	filtered = []
	for i in range(0, len(all_games)):
		if(all_games[i].date == d):
			filtered.append(all_games[i])
			template = loader.get_template('outcomes/index.html')
			context = {
				'all_games': filtered,
			}
	return HttpResponse(template.render(context, request))

def homepage(request):
	all_games = OutCome.objects.all()

	d = datetime.date(2017,10,1)

	year = d.year
	month = d.month
	day = d.day

	filtered = []
	dates = []
	intro = "EloStat predicts the outcomes of Major League Baseball games. Games are ordered by date below. Predictions can be accessed by clicking a listed date below."

	for g in range(0, len(all_games)):
		if(all_games[g].date > d):
			if(all_games[g].date not in dates):
				filtered.append(all_games[g])
			dates.append(all_games[g].date)
			template = loader.get_template('outcomes/latest.html')
			context = {
				'all_games': filtered,
				'message': intro,
			}
	return HttpResponse(template.render(context, request))
