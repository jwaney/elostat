from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from outcomes.models import OutCome


def homepage(request):
	all_games = OutCome.objects.all() 
	template = loader.get_template('outcomes/index.html')
	context = {
		'all_games': all_games,
	}
	return HttpResponse(template.render(context, request))