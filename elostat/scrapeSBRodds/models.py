from django.db import models


class Game(models.Model):
	date 	      = models.DateField()

        team_away      = models.CharField()
        away_pinnacle  = models.IntegerField()
        away_5dimes    = models.IntegerField()
        away_bookmaker = models.IntegerField()
        away_betonline = models.IntegerField()
        away_bovada    = models.IntegerField()
        away_heritage  = models.IntegerField()
        away_intertops = models.IntegerField()
        away_youwager  = models.IntegerField()
        away_justbet   = models.IntegerField()
        away_betdsi    = models.IntegerField()

        team_home      = models.CharField()
        home_pinnacle  = models.IntegerField()
        home_5dimes    = models.IntegerField()
        home_bookmaker = models.IntegerField()
        home_betonline = models.IntegerField()
        home_bovada    = models.IntegerField()
        home_heritage  = models.IntegerField()
        home_intertops = models.IntegerField()
        home_youwager  = models.IntegerField()
        home_justbet   = models.IntegerField()
        home_betdsi    = models.IntegerFiels()
