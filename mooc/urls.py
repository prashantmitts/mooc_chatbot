from django.conf.urls import url
from mooc.views import *
from mooc_chatbot import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search$', search, name='search'),
    url(r'^topic/$', topic, name='topic'),
]