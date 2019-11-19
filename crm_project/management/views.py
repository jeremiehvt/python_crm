from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Resource, Mission, Client, Company
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
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

# todo delete this part and create formset to create one ressource
class ResourceCreate(CreateView):
    template_name_suffix = '_form_view'
    template_name = 'management/forms/ressource_create_form_view.html'
    model = Resource
    http_method_names = ['get', 'put', 'head', 'option', 'trace']
    fields = [
        'job',
        'address',
        'languages',
        'tools',
        'coments',
        'user',
        'company',
        'mission'
    ]

    def get_success_url(self):
        #add flash msg tyo session
        messages.add_message(self.request, messages.INFO, 'ressource created')

        #use reverse_lazy to resolve url before loading url conf
        return reverse_lazy('crm:index')

class UserCreate(CreateView):
    http_method_names = ['get', 'put', 'head', 'option', 'trace']
    template_name_suffix = '_form_view'
    template_name = 'management/forms/user_create_form_view.html'
    model = get_user_model()
    fields = ['is_superuser', 'first_name', 'last_name', 'username', 'email', 'password', 'is_staff', 'is_active', 'groups', 'user_permissions']

    def get_success_url(self):
        #add flash msg tyo session
        messages.add_message(self.request, messages.INFO, 'user created')

        #use reverse_lazy to resolve url before loading url conf
        return reverse_lazy('crm:index')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['username'] = 'jeremiehvt'