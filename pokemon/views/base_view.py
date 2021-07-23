from django.views import generic
from django.shortcuts import render
from django.contrib.auth import get_user_model

from pokemon.funcs.decorators import get_user, handle_error, validating_db
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

    @get_user
    @validating_db
    @handle_error
    def get(self, request, user):
        pokemon = self.__get_pokemon_from_db(self.auth_user)
        if request.GET.get("pokemon"):
            context = get_pokemon(request.GET.get("pokemon"))
            self.__check_delete_pokemon_and_save(pokemon, self.auth_user, context["name"])
            return render(
                    request, 
                    "pokemon/profile.html",
                    {"user": self.auth_user,
                    "pokemon": pokemon,
                    **context}
                    )
        return render(
            request, 
            "pokemon/profile.html",
            {"user": User.objects.get(id=user),
            "pokemon": pokemon}
            )

