from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.generic import ListView, TemplateView, DetailView
from .models import UserManage, Resource, Mission, Client, Company
from .utils import Meteo

class ResourceList(ListView):
    http_method_names = ['get', 'head', 'option', 'trace']
    model = Resource
    template_name = 'management/resource_list.html'
    context_object_name = 'resources'

class IndexView(TemplateView):
    http_method_names = ['get', 'head', 'option', 'trace']
    template_name = 'management/index_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meteo = Meteo()
        missions = Mission.objects.filter(in_progress=True)
        context['meteo'] = meteo.get_meteo()
        context['mission_in_progress'] = missions
        return context

class MissionList(ListView):
    http_method_names = ['get', 'head', 'option', 'trace']
    model = Mission
    template_name = 'management/mission_list.html'
    context_object_name = 'missions'

class ClientList(ListView):
    http_method_names = ['get', 'head', 'option', 'trace']
    model = Mission
    template_name = 'management/client_list.html'
    context_object_name = 'clients'

class MissionDetail(DetailView):
    pass

class ResourceDetail(DetailView):
    pass

class ClientDetail(DetailView):
    pass
