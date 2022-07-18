from pyexpat import model

from attr import fields
from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("id", "player", "played", "wins",
                  "loss", "points", "day_played")
