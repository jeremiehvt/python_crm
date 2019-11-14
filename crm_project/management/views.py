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

        # don't forget prefetch_related or selected_related name
        # for decrease SQL request in ddb and increase performance
        missions = Mission.objects.filter(in_progress=True).prefetch_related('r_mission').order_by('-end_at')[:10]
        meteo = Meteo()
        
        context['meteo'] = meteo.get_meteo()
        context['mission_in_progress'] = missions
        return context

class MissionList(ListView):
    http_method_names = ['get', 'head', 'option', 'trace']
    model = Mission
    template_name = 'management/mission_list.html'
    context_object_name = 'missions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'test'
        return context

class ClientList(ListView):
    http_method_names = ['get', 'head', 'option', 'trace']
    model = Client
    template_name = 'management/client_list.html'
    context_object_name = 'clients'

class CompanyList(ListView):
    http_method_names = ['get', 'head', 'option', 'trace']
    model = Company
    template_name = 'management/company_list.html'
    context_object_name = 'company'

class MissionDetail(DetailView):
    http_method_names = ['get', 'head', 'option', 'trace']
    query_pk_and_slug = True
    pk_url_kwarg = 'id'
    template_name = 'management/detail.html'
    context_object_name = 'details'

    def get_queryset(self):
        return Mission.objects.filter(pk=self.kwargs['id']).prefetch_related('r_mission')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classname'] = self.__class__.__name__
        return context

class ResourceDetail(DetailView):
    http_method_names = ['get', 'head', 'option', 'trace']
    query_pk_and_slug = True
    pk_url_kwarg = 'id'
    template_name = 'management/detail.html'
    context_object_name = 'details'

    def get_queryset(self):
        return Resource.objects.filter(pk=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classname'] = self.__class__.__name__
        return context

class ClientDetail(DetailView):
    http_method_names = ['get', 'head', 'option', 'trace']
    query_pk_and_slug = True
    pk_url_kwarg = 'id'
    template_name = 'management/detail.html'
    context_object_name = 'details'

    def get_queryset(self):
        return Client.objects.filter(pk=self.kwargs['id']).prefetch_related('m_client')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classname'] = self.__class__.__name__
        return context

class CompanyDetail(DetailView):
    http_method_names = ['get', 'head', 'option', 'trace']
    query_pk_and_slug = True
    pk_url_kwarg = 'id'
    template_name = 'management/detail.html'
    context_object_name = 'details'

    def get_queryset(self):
        return Company.objects.filter(pk=self.kwargs['id']).prefetch_related('r_company')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classname'] = self.__class__.__name__
        return context