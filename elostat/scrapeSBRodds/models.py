from django.db import models

class Game(models.Model):
	date		= models.DateField()
	game_id		= models.IntegerField()

	score_away	= models.IntegerField()
	team_away	= models.CharField(max_length=20)
	away_pinnacle	= models.IntegerField()
	away_5dimes	= models.IntegerField()
	away_bookmaker	= models.IntegerField()
	away_betonline	= models.IntegerField()
	away_bovada	= models.IntegerField()
	away_heritage	= models.IntegerField()
	away_intertops	= models.IntegerField()
	away_youwager	= models.IntegerField()
	away_justbet	= models.IntegerField()
	away_betdsi	= models.IntegerField()

	score_home	= models.IntegerField()
	team_home	= models.CharField(max_length=20)
	home_pinnacle	= models.IntegerField()
	home_5dimes	= models.IntegerField()
	home_bookmaker	= models.IntegerField()
	home_betonline	= models.IntegerField()
	home_bovada	= models.IntegerField()
	home_heritage	= models.IntegerField()
	home_intertops	= models.IntegerField()
	home_youwager	= models.IntegerField()
	home_justbet	= models.IntegerField()
	home_betdsi	= models.IntegerField()

	def __str__(self):
		return str(self.date) + " " + str(self.team_away) + " VS " + str(self.team_home)
