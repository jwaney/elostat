from django.shortcuts import render,redirect

from django.template import loader
from django.http import HttpResponse
from outcomes.models import OutCome
import datetime
from datetime import date


def homepage(request, date_game):
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
