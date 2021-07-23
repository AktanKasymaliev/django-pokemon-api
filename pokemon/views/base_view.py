from django.contrib import messages
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import get_user_model

from pokemon.funcs.decorators import handle_error
from pokemon.models import Pokemon
from pokemon.funcs.pokemons import get_pokemon

User = get_user_model()

class BaseView(generic.View):
    
    def get(self, request):
        return render(
            request, 
            "pokemon/home.html", 
            {"request_user": request.user.id}
            )

class MyProfileView(generic.View):
    
    def __save_pokemon_to_db(self, user: User, pokemon_name: str) -> None:
        return Pokemon.objects.create(user=user, pokemon=pokemon_name)

    def __get_pokemon_from_db(self, user):
        try:
            return Pokemon.objects.get(user=user)
        except:
            return None

    def __check_delete_pokemon_and_save(self, pokemon: Pokemon, user: User, pokemon_name: str) -> None:
        if pokemon is None:
            self.__save_pokemon_to_db(user, pokemon_name)
        else:
            pokemon.delete(), self.__save_pokemon_to_db(user, pokemon_name)

    @handle_error
    def get(self, request, user):
        auth_user = User.objects.get(id=user)
        pokemon = self.__get_pokemon_from_db(user)
        if request.GET.get("pokemon"):
            context = get_pokemon(request.GET.get("pokemon"))
            self.__check_delete_pokemon_and_save(pokemon, auth_user, context["name"])
            return render(
                    request, 
                    "pokemon/profile.html",
                    {"user": auth_user,
                    "pokemon": pokemon,
                    **context}
                    )
        return render(
            request, 
            "pokemon/profile.html",
            {"user": User.objects.get(id=user),
            "pokemon": pokemon}
            )

#TODO Сделать Удаление с БД Покемона если тот уже существует