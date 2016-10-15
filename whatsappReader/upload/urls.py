from django.conf.urls import url
from upload.views import *
urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^read_latest/$', readfile,name='readfile'),
]
