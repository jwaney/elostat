from django.db import models

class OutCome(models.Model):
	date		= models.DateField()
	game_id		= models.IntegerField()

	team_away	= models.CharField(max_length=20)
	team_home	= models.CharField(max_length=20)

	prediction	= models.FloatField()

	def __str__(self):
		return str(self.date) + " " + str(self.team_away) + " VS " + str(self.team_home)