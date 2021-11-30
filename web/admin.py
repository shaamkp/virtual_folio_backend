from django.contrib import admin
from web.models import Contact
from web.models import Subscribe



admin.site.register(Subscribe)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email","subject","message"]
admin.site.register(Contact)
