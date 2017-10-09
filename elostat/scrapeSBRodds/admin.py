from django.contrib import admin
from scrapeSBRodds.models import Game

class GameAdmin(admin.ModelAdmin):
	list_display = ('game_id', 'team_away', 'score_away', 'team_home', 'score_home', 'date')

admin.site.register(Game, GameAdmin)
