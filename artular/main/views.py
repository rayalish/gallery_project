from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import *
# Create your views here.

class Home(View):
    def get(self, request):
        artworks = Artwork.objects.all()
        authors = Author.objects.all()

        context = {
            'title': 'Welcome',
            'artworks': artworks,
            'authors': authors,

        }

        return render(request, 'main/home_page.html', context=context)