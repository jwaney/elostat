from django.db import models

class OutCome(models.Model):
	date		= models.DateField()
	game_id		= models.IntegerField(primary_key=True)

	team_away	= models.CharField(max_length=20)
	team_home	= models.CharField(max_length=20)

	pred_away	= models.CharField(max_length=20)
	pred_home	= models.CharField(max_length=20)

	def __str__(self):
		return str(self.date) + " " + str(self.team_away) + " VS " + str(self.team_home)
