from django.db import models

# Create your models here.

class UserManage(models.Model):
    class Meta:
        abstract = True
    firstName = models.CharField('prénom', max_length=100, blank=False, null=False)
    lastName = models.CharField('nom', max_length=100, blank=False, null=False)
    email = models.EmailField('email', max_length=100, null=True, unique=True, blank=False)
    address = models.CharField('adresse', max_length=100, blank=False, null=True)

class Company(models.Model):
    class Meta:
        verbose_name = 'entité'
        verbose_name_plural = 'entités'
    name = models.CharField('nom', max_length=100, blank=False, null=False)
    address = models.CharField('adresse', max_length=100, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.name)

class Resource(UserManage):
    class Meta:
        verbose_name = 'ressource'
        verbose_name_plural = 'ressources'
    job = models.CharField('métier', max_length=100, blank=False, null=False, default='')
    company = models.OneToOneField(Company, on_delete=False, null=True)

    def __str__(self):
        return "{0} {1}".format(self.firstName, self.lastName)
    
class Mission(models.Model):
    class Meta:
        verbose_name = 'mission'
        verbose_name_plural = 'missions'
    begin_at = models.DateTimeField('début de la mission',null=True)
    end_at = models.DateTimeField('fin de la mission',null=True)
    codeName = models.CharField('nom de code', max_length=200, blank=False, null=False, default='')
    description = models.TextField('description', blank=False, null=True)
    resources = models.ForeignKey(Resource, on_delete=False, null=True)

    def __str__(self):
        return "{}".format(self.codeName)


class Client(models.Model):
    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
    name = models.CharField('nom', max_length=100, blank=False, null=False)
    address = models.CharField('adresse', max_length=100, blank=False, null=False)
    missions = models.ForeignKey(Mission, on_delete=False, null=True)

    def __str__(self):
        return "{}".format(self.name)
