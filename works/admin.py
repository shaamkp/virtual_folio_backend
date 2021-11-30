from django.contrib import admin
from works.models import Catagory
from works.models import Service, Project


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "title", "description"]

    admin.site.register(Service)

    admin.site.register(Project)

    admin.site.register(Catagory)