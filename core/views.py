from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context ={
            
        }                     
        #index.html home into templates
        return render(request, "index.html",context)