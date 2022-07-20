from django.urls import path
from .views import GameView
from . import views

urlpatterns = [
    path("Game", GameView.as_view()),
]
