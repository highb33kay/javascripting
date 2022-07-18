from datetime import datetime
from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=255)


class Game(models.Model):
    player = models.ForeignKey(
        Player, verbose_name='player', on_delete=models.CASCADE)
    wins = models.IntegerField(verbose_name='wins')
    loss = models.IntegerField(verbose_name="loss")
    points = models.IntegerField(verbose_name='points')
    day_played = models.DateField(
        default=datetime.today, verbose_name="date")
