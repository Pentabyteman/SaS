"""sas_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^$', include('startpage.urls', namespace='startpage', app_name='startpage')),
    url(r'^meingoethopia', include('meingoethopia.urls',
                                   namespace='meingoethopia',
                                   app_name='meingoethopia')),
    url(r'^datenbank', include('datenbank.urls', app_name='datenbank',
                               namespace='datenbank')),
    url(r'^admin/', include(admin.site.urls)),
]
