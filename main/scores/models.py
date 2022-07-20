from datetime import date
from django.db import models


# class Player(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


class Game(models.Model):
    player = models.CharField(
        max_length=255, verbose_name='player')
    wins = models.IntegerField(verbose_name='wins', default=0)
    loss = models.IntegerField(verbose_name="loss", default=0)
    points = models.IntegerField(verbose_name='points', default=0)
    day_played = models.DateField(default=date.today())
    played = models.IntegerField(verbose_name="played", default=0)

    def __str__(self) -> str:
        return str(self.player)
    # Create your models here.
