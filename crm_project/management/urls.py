from django.urls import path
from . import views
from .views import ResourceList, IndexView

# setting app name to use namsepace
app_name='crm'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('resources', ResourceList.as_view(), name='allResources'),
    path('missions', views.allMissions, name='allMissions'),
]
