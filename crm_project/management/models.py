from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Company(models.Model):
    class Meta:
        verbose_name = 'entité'
        verbose_name_plural = 'entités'
    name = models.CharField('nom', max_length=100, blank=False, null=False)
    address = models.CharField('adresse', max_length=100, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.name)

class Client(models.Model):
    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
    name = models.CharField('nom', max_length=100, blank=False, null=False)
    address = models.CharField('adresse', max_length=100, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.name)

class Mission(models.Model):
    class Meta:
        verbose_name = 'mission'
        verbose_name_plural = 'missions'
    begin_at = models.DateField('début de la mission', null=True)
    end_at = models.DateField('fin de la mission', null=True)
    in_progress = models.BooleanField('en cours', default=False, null=False)
    code_name = models.CharField('nom de code', max_length=200, blank=False, null=False, default='')
    description = models.TextField('description', blank=False, null=True)
    # don't forget related name and related_query_name for inverse models relations and 
    # avoid xxx_set method. See in django doc https://docs.djangoproject.com/en/2.2/topics/db/queries/ for more informations
    # this comment is avilable for other foreignkey case in this script
    client = models.ForeignKey(Client, on_delete=False, null=True, related_name='m_client', related_query_name='m_clients')

    def __str__(self):
        return "{}".format(self.code_name)

class Resource(models.Model):
    class Meta:
        verbose_name = 'ressource'
        verbose_name_plural = 'ressources'
    job = models.CharField('métier', max_length=100, blank=False, null=False, default='')
    address = models.CharField('adresse', max_length=100, blank=False, null=True)
    languages = models.CharField('langues parlées', max_length=200, blank=True, null=True, default='')
    tools = models.CharField('outils informatiques', max_length=200, blank=True, null=True, default='')
    coments = models.TextField('commentaires', blank=True, null=True)
    user = models.OneToOneField(get_user_model(), on_delete=True, null=False, related_name='r_user', related_query_name='r_users')
    company = models.ForeignKey(Company, on_delete=False, null=True, related_name='r_company', related_query_name='r_companies')
    mission = models.ForeignKey(Mission, on_delete=False, null=True, related_name='r_mission', related_query_name='r_missions')

    def __str__(self):
        return "{0}".format(self.job)
