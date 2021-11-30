from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("web.urls",namespace="web")),
    path("",include("users.urls",namespace="users")),
    path("",include("works.urls",namespace="works")),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)