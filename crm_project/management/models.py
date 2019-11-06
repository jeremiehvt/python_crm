from django.db import models

# Create your models here.

class UserManage(models.Model):

    firstName = models.CharField('prénom', max_length=100, blank=False, null=False)
    lastName = models.CharField('nom', max_length=100, blank=False, null=False)
    email = models.EmailField('email', max_length=100, null=True, unique=True, blank=False)
    address = models.CharField('adresse', max_length=100, blank=False, null=True)

class Company(models.Model):
    
    name = models.CharField('entité', max_length=100, blank=False)
    address = models.CharField('adresse', max_length=100, blank=False)

class Resource(UserManage):

    job = models.CharField('métier', max_length=100, blank=False)
    company = models.OneToOneField(Company, on_delete=False)
    
class Mission(models.Model):

    begin_at = models.DateField('début de la mission')
    end_at = models.DateField('fin de la mission')
    resources = models.ForeignKey(Resource, on_delete=False)

class Client(models.Model):
    missions = models.ForeignKey(Mission, on_delete=False)