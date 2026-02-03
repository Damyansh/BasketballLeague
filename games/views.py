from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def game_add(request: HttpRequest)-> HttpResponse:
    return render(request, 'games/game-add-page.html')

def game_edit(request: HttpRequest)-> HttpResponse:
    return render(request, 'games/game-edit-page.html')

def game_details(request: HttpRequest)-> HttpResponse:
    return render(request, 'games/game-details-page.html')