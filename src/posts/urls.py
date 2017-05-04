from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^(?P<id>[0-9]+)/$', views.post_detail, name='detail'),
    url(r'^(?P<id>[0-9]+)/update/$', views.post_update, name='update'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.post_delete, name='delete'),
]