from django import forms
from .models import Resource
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.forms import inlineformset_factory, ModelForm
from django.contrib.auth import get_user_model

class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['is_superuser', 'first_name', 'last_name', 'username', 'email', 'password', 'is_staff', 'is_active', 'groups', 'user_permissions']