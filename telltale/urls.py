from django.conf.urls import include, url
from django.contrib import admin
from stories.views import StoryListView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^story/', include('stories.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^$', StoryListView.as_view()),
]
