from django.db import models
from .game_type import Game_Type
from .gamer import Gamer


class Game(models.Model):

    game_type = models.ForeignKey(
        Game_Type, on_delete=models.PROTECT
    )  # Prevent deletion of Game_Type
    title = models.CharField(max_length=75)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey(
        Gamer, on_delete=models.PROTECT
    )  # Prevent deletion of Gamer
    number_of_players = models.PositiveIntegerField()  # Restrict to positive Integers
    skill_level = models.PositiveIntegerField()  # Restrict to positive Integers
