from django.contrib import admin
from .models import Resource, Client, Mission, Company
# Register your models here.

admin.site.register(Resource)
admin.site.register(Client)
admin.site.register(Mission)
admin.site.register(Company)