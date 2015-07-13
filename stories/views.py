from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from django.conf import settings
from braces.views import LoginRequiredMixin
from stories.forms import StoryChunkWriteForm, StoryJoinForm
from stories.models import Story, StoryChunk


class StoryListView(LoginRequiredMixin, TemplateView):
    template_name = 'list-stories.html'

    def get_context_data(self):
        data = super(LoginRequiredMixin, self).get_context_data()
        data.update({
            'unfinished_stories': self.request.user.stories.filter(finished=False),
            'finished_stories': self.request.user.stories.filter(finished=True),
        })
        return data


class StoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new-story.html'
    model = StoryChunk
    form_class = StoryChunkWriteForm
    success_url = reverse_lazy('list-stories')

    def form_invalid(self, form):
        import ipdb; ipdb.set_trace()

    def get_form_kwargs(self):
        kwargs = super(StoryCreateView, self).get_form_kwargs()
        kwargs.update({'author': self.request.user})
        return kwargs

    def get_context_data(self, *args, **kwargs):
        data = super(StoryCreateView, self).get_context_data(*args, **kwargs)
        data.update({
            'settings': settings,
        })
        return data


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

    def get_form_kwargs(self):
        kwargs = super(StoryWriteView, self).get_form_kwargs()
        kwargs.update({
            'author': self.request.user,
            'story': self.get_story(),
        })
        return kwargs

    def get_context_data(self, *args, **kwargs):
        data = super(StoryWriteView, self).get_context_data(*args, **kwargs)
        story = self.get_story()
        data.update({
            'settings': settings,
            'story': story,
            'final': story.chunks.count() == story.num_chunks - 1,
        })
        return data


class StoryJoinView(LoginRequiredMixin, FormView):
    template_name = 'join-story.html'
    form_class = StoryJoinForm


class StoryReadView(LoginRequiredMixin, DetailView):
    template_name = 'read-story.html'
    model = Story
