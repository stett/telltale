from django.conf.urls import include, url
from django.contrib import admin
from users import views

urlpatterns = [
    url(r'new/$', views.signup, name='new-account'),
    url(r'signin/$', views.signin, name='signin'),
    url(r'settings/$', views.settings, name='user-settings'),
]
