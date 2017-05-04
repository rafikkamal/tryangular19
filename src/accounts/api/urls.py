from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.PostListAPIView.as_view(), name='index'),
    url(r'^register/$', views.UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', views.UserLoginAPIView.as_view(), name='login'),
    #url(r'^(?P<id>[0-9]+)/edit/$', views.PostUpdateAPIView.as_view(), name='update'),
    #url(r'^(?P<id>[0-9]+)/delete/$', views.PostDeleteAPIView.as_view(), name='delete'),


    # url(r'^create/$', views.post_create, name='create'),
    # url(r'^(?P<id>[0-9]+)/$', views.post_detail, name='detail'),
    # url(r'^(?P<id>[0-9]+)/update/$', views.post_update, name='update'),
    # url(r'^delete/$', views.post_delete, name='delete'),
]