from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def player_add(request: HttpRequest)-> HttpResponse:
    return render(request, 'players/player-add-page.html')

def player_edit(request: HttpRequest, pk:int)-> HttpResponse:
    return render(request, 'players/player-edit-page.html')

def player_delete(request: HttpRequest, pk:int)-> HttpResponse:
    return render(request, 'players/player-delete-page.html')

def player_details(request: HttpRequest, pk:int)-> HttpResponse:
    return render(request, 'players/player-details-page.html')