from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def team_add(request: HttpRequest)-> HttpResponse:
    return render(request, 'teams/team-add-page.html')

def team_details(request: HttpRequest, pk:int)-> HttpResponse:
    return render(request, 'teams/team-details-page.html')

def team_edit(request: HttpRequest, pk:int)-> HttpResponse:
    return render(request, 'teams/team-edit-page.html')

def team_delete(request: HttpRequest, pk:int)-> HttpResponse:
    return render(request, 'teams/team-delete-page.html')