from functools import wraps

from django.shortcuts import render

def handle_error(func):
    @wraps(func)
    def wrapper(obj, *args, **kwargs):
        try:
            return func(obj, *args, **kwargs)
        except Exception:
            return render(*args, "errors/error.html")
    return wrapper