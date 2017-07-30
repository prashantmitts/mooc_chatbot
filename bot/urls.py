from django.conf.urls import url
from bot.views import user_list


urlpatterns = [
    url(r'^$', user_list, name='user_list'),
]