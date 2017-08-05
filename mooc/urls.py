from django.conf.urls import url
from mooc.views import *


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search$', search, name='search'),
    url(r'^topic/$', topic, name='topic'),
]