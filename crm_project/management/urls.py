from django.urls import path, include
from . import views
from .views import \
    ResourceList, \
    IndexView, \
    MissionList, \
    CompanyList, \
    ClientDetail, \
    ClientList, \
    CompanyDetail, \
    ResourceDetail, \
    MissionDetail, \
    ResourceCreate, \
    UserCreate

# setting app name to use namsepace
app_name = 'crm'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('resources/', ResourceList.as_view(), name='all_resources'),
    path('missions/', MissionList.as_view(), name='all_missions'),
    path('clients/', ClientList.as_view(), name='all_clients'),
    path('companies/', CompanyList.as_view(), name='all_companies'),
    path('<int:id>/', include([
        path('client/', ClientDetail.as_view(), name='detail_client'),
        path('company/', CompanyDetail.as_view(), name='detail_company'),
        path('mission/', MissionDetail.as_view(), name='detail_mission'),
        path('ressource/', ResourceDetail.as_view(), name='detail_resource'),
    ])),
    path('create_resource/', ResourceCreate.as_view(), name='create_resource'),
    path('create_user/', UserCreate.as_view(), name='create_user'),
]
