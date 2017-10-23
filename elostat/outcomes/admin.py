from django.contrib import admin
from outcomes.models import OutCome

class OutComeAdmin(admin.ModelAdmin):
	list_display = ('game_id', 'date', 'team_away', 'pred_away', 'team_home', 'pred_home')

admin.site.register(OutCome, OutComeAdmin)
