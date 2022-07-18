from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GameSerializer
from .models import Game

# Create your views here.


class GameViewSet(GameModelViewSet):
    Serializer_class = GameSerializer
    query_set = Game.objects.all()

# def score(request):
#     return render(request, "scores/scores.html")
