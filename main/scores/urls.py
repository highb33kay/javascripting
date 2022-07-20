from django.urls import path
from .views import GameView
from . import views

urlpatterns = [
    path("home", GameView.as_view()),
]
