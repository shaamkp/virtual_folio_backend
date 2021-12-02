from django import forms
from django.forms import ModelForm, fields
from works.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields="__all__"
        
