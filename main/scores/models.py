from datetime import datetime
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):
    player = models.ForeignKey(
        Player, verbose_name='player', on_delete=models.CASCADE)
    wins = models.IntegerField(verbose_name='wins', default=0)
    loss = models.IntegerField(verbose_name="loss", default=0)
    points = models.IntegerField(verbose_name='points', default=0)
    day_played = models.DateField(
        default=datetime.today, verbose_name="date")
    played = models.IntegerField(verbose_name="played", default=0)

    def __str__(self) -> str:
        return str(self.player)
    # Create your models here.
