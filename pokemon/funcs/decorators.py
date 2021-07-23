from functools import wraps

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon

User = get_user_model()

def handle_error(func):
    @wraps(func)
    def wrapper(obj, *args, **kwargs):
        try:
            return func(obj, *args, **kwargs)
        except Exception as e:
            print(e)
            return render(*args, "errors/error.html")
    return wrapper

def get_user(func):
    @wraps(func)
    def wrapper(obj, *args, **kwargs):
        obj.auth_user = User.objects.get(id=kwargs.get("user", None)) 
        return func(obj, *args, **kwargs)
    return wrapper

def validating_db(func) -> HttpResponse:
    @wraps(func)
    def wrapper(obj, *args, **kwargs):
        if Pokemon.objects.filter(user=obj.auth_user).count() >= 2:
            return render(*args, "errors/error401.html")
        else:
            return func(obj, *args, **kwargs)
    return wrapper