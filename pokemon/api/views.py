from rest_framework import generics
from django.contrib.auth import get_user_model

from pokemon.api.serializers import UsersSerializers, PokemonsSerializers
from pokemon.models import Pokemon

User = get_user_model()

class UsersAPIView(generics.ListAPIView):
    model = User
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UsersSerializers

class PokemonsAPIView(generics.ListAPIView):
    model = Pokemon
    queryset = Pokemon.objects.select_related("user")
    serializer_class = PokemonsSerializers