from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
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
        kwargs = super(StoryCreateView, self).get_form_kwargs()
        kwargs.update({'author': self.request.user})
        return kwargs


class StoryJoinView(LoginRequiredMixin, FormView):
    template_name = 'join-story.html'
    form_class = StoryJoinForm


class StoryWriteView(LoginRequiredMixin, CreateView):
    template_name = 'write-story.html'
    model = StoryChunk


class StoryReadView(LoginRequiredMixin, DetailView):
    template_name = 'read-story.html'
    model = Story
