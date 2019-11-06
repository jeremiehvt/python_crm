from django.urls import path
from . import views

# setting app name to use namsepace
app_name='crm'

urlpatterns = [
    path('', views.index, name='index'),
    path('resources', views.allResources, name='allResources'),
    path('missions', views.allMissions, name='allMissions'),
]
