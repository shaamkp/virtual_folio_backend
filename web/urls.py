from django.urls import path
from web.views import index,subscribe,contact,category



app_name = "web"


urlpatterns = [
    path("",index, name="index"),
    path("category/",category, name="category"),
    path("subscribe/",subscribe, name="subscribe"),
    path("contact/",contact, name="contact")
]


