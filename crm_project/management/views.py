from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
import requests


def index(request):
    return HttpResponse("voici la première page du crm en version basic html bienvenue")

def allResources(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/crm/")

def allMissions(request):
    payload = {'q': {'London', 'uk'}, 'APPID': '43d45b6981ca6beef6f552c4ba738074'}
    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    
    return HttpResponse(r)

def singleMission(request):
    pass

def singleResource(request):
    pass

def allClients(request):
    pass

def singleClient(request):
    pass