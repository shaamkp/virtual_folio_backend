from django.shortcuts import render
from django.http import HttpResponse
from works.models import Project,Service


def index(request):
    projects = Project.objects.all()
    services = Service.objects.all()

    context = {
        "projects" : projects,
        "services" : services,
    }
    
    return render,HttpResponse(request,"index.html",context=context)

