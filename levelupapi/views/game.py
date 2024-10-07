"""View module for handling requests about game types"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, Game_Type


class GameView(ViewSet):
    """Level up games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game

        Returns:
            Response -- JSON serialized list of game
        """
        games = Game.objects.all()
        game_type = request.query_params.get("type", None)
        if game_type is not None:
            games = games.filter(game_type_id=game_type)

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
         Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(uid=request.data["userId"])
        game_type = Game_Type.objects.get(pk=request.data["game_type"])

        game = Game.objects.create(
            title=request.data["title"],
            maker=request.data["maker"],
            number_of_players=request.data["number_of_players"],
            skill_level=request.data["skill_level"],
            game_type=game_type,
            gamer=gamer,
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types"""

    class Meta:
        model = Game
        fields = (
            "id",
            "game_type",
            "title",
            "maker",
            "gamer",
            "number_of_players",
            "skill_level",
        )
        depth = 1
