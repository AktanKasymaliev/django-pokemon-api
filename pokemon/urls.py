from django.urls import path

from pokemon.views.auth import (RegisterView, 
                                LogInView, 
                                LogOutView)
from pokemon.views.base_view import BaseView

urlpatterns = [
    path("", BaseView.as_view(), name="home"),

    path("signup/user/", RegisterView.as_view(), name='signup'),
    path("login/user/", LogInView.as_view(), name="login"),
    path("logout/user/", LogOutView.as_view(), name="logout")
]