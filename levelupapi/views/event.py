"""View module for handling requests about game types"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer


class EventView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        game = Game.objects.get(pk=request.data["game"])
        organizer = Gamer.objects.get(uid=request.data["userId"])
        event = Event.objects.create(
            description=request.data["description"],
            game=game,
            date=request.data["date"],
            time=request.data["time"],
            organizer=organizer,
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""

    class Meta:
        model = Event
        fields = ("id", "game", "description", "date", "time", "organizer")
        depth = 2
