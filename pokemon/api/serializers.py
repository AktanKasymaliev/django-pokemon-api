import re
from pokemon.models import Pokemon
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class PokemonsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Pokemon
        fields = ("id", "user", "pokemon")

class UsersSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "username")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user\'s_pokemon'] = PokemonsSerializers(instance.user.all(), many=True).data
        return representation