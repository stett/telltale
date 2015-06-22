from django.conf.urls import include, url
from django.contrib import admin
from stories import views

urlpatterns = [
    url(r'list/$', views.list_stories_view, name='list-stories'),
    url(r'new/$', views.new_story_view, name='new-story'),
    url(r'join/(?P<pk>\d+)/$', views.join_story_view, name='join-story'),
    url(r'write/(?P<pk>\d+)/$', views.write_story_view, name='write-story'),
    url(r'read/(?P<pk>\d+)/$', views.read_story_view, name='read-story'),
]
