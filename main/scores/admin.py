from django.contrib import admin
from .models import Game, Player
# Register your models here.


class GameAdmin(admin.ModelAdmin):
    list_display = ("player", "played", "wins", "loss", "points", "day_played")


admin.site.register(Game, GameAdmin)
admin.site.register(Player)
