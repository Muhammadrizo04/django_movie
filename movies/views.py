from django.shortcuts import render
from django.views.generic.base import View
from .models import *

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movie_list.html", {"movies_list": movies})