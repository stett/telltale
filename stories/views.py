from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from django.conf import settings
from braces.views import LoginRequiredMixin
from stories.forms import StoryChunkWriteForm, StoryJoinForm
from stories.models import Story, StoryChunk


class StoryListView(LoginRequiredMixin, ListView):
    template_name = 'list-stories.html'
    context_object_name = 'stories'
    model = Story


class StoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new-story.html'
    model = StoryChunk
    form_class = StoryChunkWriteForm
    success_url = reverse_lazy('list-stories')

    def get_form_kwargs(self):
        return {'author': self.request.user}


class StoryWriteView(LoginRequiredMixin, CreateView):
    template_name = 'write-story.html'
    model = StoryChunk
    form_class = StoryChunkWriteForm
    success_url = reverse_lazy('list-stories')

    def __init__(self):
        super(StoryWriteView, self).__init__()
        self.story = None

    def get_story(self):
        if not self.story:
            self.story = Story.objects.get(pk=self.kwargs.get('pk'))
        return self.story

    def get_leadin(self):
        return self.get_story().get_last_chunk().get_leadin()

    def get_settings(self):
        return settings

    def get_form_kwargs(self):
        return {
            'author': self.request.user,
            'story': self.get_story()}


class StoryJoinView(LoginRequiredMixin, FormView):
    template_name = 'join-story.html'
    form_class = StoryJoinForm


class StoryReadView(LoginRequiredMixin, DetailView):
    template_name = 'read-story.html'
    model = Story
