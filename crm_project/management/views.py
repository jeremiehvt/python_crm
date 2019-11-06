from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import urllib
# Create your views here.

def index(request):
    return HttpResponse("voici la première page du crm en version basic html bienvenue")

def allResources(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/crm/")

def allMissions(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/crm/")
    
def singleMission(request):
    pass

def singleResource(request):
    pass

def allProjects(request):
    pass

def singleProject(request):
    pass