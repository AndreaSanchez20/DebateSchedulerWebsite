#convert the python objects to JSON objects
from rest_framework import serializers
from debateApp.models import Round2
from debateApp.models import Tournament
from debateApp.models import Note
from debateApp.models import LoginAuth

class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round2
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class LoginAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginAuth
        fields = '__all__'