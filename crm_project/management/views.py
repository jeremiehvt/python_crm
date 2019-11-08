from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.generic import ListView, TemplateView, DetailView
import requests
from .models import UserManage, Resource, Mission, Client, Company

class ResourceList(ListView):
    http_method_names = ['get','head','option','trace']
    model = Resource
    template_name = 'management/resource_list.html'
    context_object_name = 'resources'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meteo'] = "voici la météo"

class IndexView(TemplateView):
    http_method_names = ['get','head','option','trace']
    template_name = 'management/index_view.html'
    context_object_name = 'homepage_infos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meteo'] = "voici la météo"

class MissionList(ListView):
    http_method_names = ['get','head','option','trace']
    model = Mission
    template_name = 'management/mission_list.html'
    context_object_name = 'missions'

class ClientList(ListView):
    http_method_names = ['get','head','option','trace']
    model = Mission
    template_name = 'management/client_list.html'
    context_object_name = 'clients'

class MissionDetail(DetailView):
    pass

class ResourceDetail(DetailView):
    pass

class ClientDetail(DetailView):
    pass

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