from django.views import generic
from django.shortcuts import render

class BaseView(generic.View):
    
    def get(self, request):
        return render(request, "pokemon/home.html")