from django.urls import path
from . import views
from .views import ResourceList, IndexView, MissionList, ClientDetail

# setting app name to use namsepace
app_name='crm'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('resources', ResourceList.as_view(), name='all_resources'),
    path('missions', MissionList.as_view(), name='all_missions'),
    path('client/<int:id>', ClientDetail.as_view(), name='detail_client'),
]
