from django.urls import path
from works.views import index
from works import views


app_name = "works"


urlpatterns = [
    # path("works/index",index, name="index"),
    path('', views.index),
]
