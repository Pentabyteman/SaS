from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^impressum', views.impressum, name='impressum'),
    url(r'^$', views.index, name='index')
]
