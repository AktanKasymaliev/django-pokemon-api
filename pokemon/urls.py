from django.urls import path

from pokemon.views.auth import (RegisterView, 
                                LogInView, 
                                LogOutView)
from pokemon.views.base_view import BaseView, MyProfileView
from pokemon.api.views import PokemonsAPIView, UsersAPIView

urlpatterns = [

    # home view 
    path("", BaseView.as_view(), name="home"),
    path("my/profile/<int:user>/", MyProfileView.as_view(), name='profile'),

    # auth 
    path("signup/user/", RegisterView.as_view(), name='signup'),
    path("login/user/", LogInView.as_view(), name="login"),
    path("logout/user/", LogOutView.as_view(), name="logout"),

    # api
    path("api/v1/users/", UsersAPIView.as_view(), name='users'),
    path("api/v1/pokemons/", PokemonsAPIView.as_view(), name='pokemons'),
    
]

#TODO 1. Unnittests 2. Docker