from django.conf.urls import include, url
from django.contrib import admin
from stories import views

urlpatterns = [
    url(r'list/$', views.StoryListView.as_view(), name='list-stories'),
    url(r'new/$', views.StoryCreateView.as_view(), name='new-story'),
    url(r'join/(?P<pk>\d+)/$', views.StoryJoinView.as_view(), name='join-story'),
    url(r'write/(?P<pk>\d+)/$', views.StoryWriteView.as_view(), name='write-story'),
    url(r'read/(?P<pk>\d+)/$', views.StoryReadView.as_view(), name='read-story'),
]
