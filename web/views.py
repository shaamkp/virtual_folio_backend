import json
import os
from django.conf import settings
from django.http import response
from django.shortcuts import render, get_object_or_404
from django.http.response import Http404, HttpResponse
from users.models import Profile,Address,Education,Experience,Skill, SkillItem, Client
from works.models import Catagory
from web.models import Subscribe,Testimonial,Contact
from works.models import Service, Project 


def index(request):
    profile = Profile.objects.get(user_id=1)
    skills = Skill.objects.filter(user_id=profile.pk)
    skill_items = SkillItem.objects.filter(skill__user_id=profile.pk)
    education = Education.objects.all()
    experience = Experience.objects.all()
    service = Service.objects.all()
    projects = Project.objects.all()
    total_clients = Client.objects.all()
    completed_project_count = projects.filter(is_completed_count=True).count()
    satisfied_client_count = projects.filter(is_satisfied_count=True).count()
    pending_projects_count = projects.filter(is_completed_count=False).count()
    catagories = Catagory.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    

    context = {
        "profile" : profile,
        "education" : education,
        "experience" : experience,
        "service" : service,
        "skills" : skills,
        "skill_items" : skill_items,
        "projects" : projects,
        "catagories" : catagories,
        "clients" : clients,
        "total_clients" : total_clients,
        "completed_project_count" :completed_project_count,
        "satisfied_client_count" :satisfied_client_count,
        "pending_projects_count" :pending_projects_count,

    }
    return render(request, "index.html",context = context)


def subscribe(request):
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email=email).exists():

        Subscribe.objects.create(
            email = email,
        )

        response_data = {
            "status" :"success",
            "message" : "You subscribed to our newsletter successfully",
            "title" : "Successfully Registered"
        }
    else:
        response_data = {
            "status" :"error",
            "message" : "You are already a member. No need to register again",
            "title" : "You are already subscribed."
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def contact(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")

    if not Contact.objects.filter(name=name).exists():

        Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )

        response_data = {
            "status" :"success",
            "message" : "Done",
            "title" : "We will contact you"
        }
    else:
        response_data = {
            "status" :"error",
            "message" : "You are already sent the message. No need to sent again",
            "title" : "We got your message."
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
    



def address(request):
    context = {
        "address" : Profile.objects.all(),
    }
    return render(request,"index.html",context=context)


def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/resume")
            response['Content-Disposition']='inline;filename=+os.path.basename(file_path)'
            return response

    raise Http404


