from django.shortcuts import render
from rest_framework import generics
from .serializers import GameSerializer
from .models import Game

# Create your views here.


class GameView(generics.ListAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

# def score(request):
#     return render(request, "scores/scores.html")
