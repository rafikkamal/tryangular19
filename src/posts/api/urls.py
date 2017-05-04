from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name='index'),
    url(r'^create/$', views.PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>[0-9]+)/$', views.PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>[0-9]+)/edit/$', views.PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.PostDeleteAPIView.as_view(), name='delete'),


    # url(r'^create/$', views.post_create, name='create'),
    # url(r'^(?P<id>[0-9]+)/$', views.post_detail, name='detail'),
    # url(r'^(?P<id>[0-9]+)/update/$', views.post_update, name='update'),
    # url(r'^delete/$', views.post_delete, name='delete'),
]