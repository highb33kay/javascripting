from django.contrib import admin
from .models import Game, Player
# Register your models here.


class GameAdmin(admin.ModelAdmin):
    list_display = ("player", "wins", "loss", "points", "day_played")


admin.site.register(Game)
admin.site.register(Player)
