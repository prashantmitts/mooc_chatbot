from django.conf.urls import url
from mooc.views import topic


urlpatterns = [
    url(r'^$', topic, name='topic'),
]