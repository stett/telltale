from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy


@login_required(login_url=reverse_lazy('signin'))
def list_stories_view(request):
    context = {
        'stories': [],
    }
    return render(request, 'list-stories.html', context)


@login_required(login_url=reverse_lazy('signin'))
def new_story_view(request):
    context = {
        'form': None,
    }
    return render(request, 'new-story.html', context)


@login_required(login_url=reverse_lazy('signin'))
def join_story_view(request, pk):
    context = {
        'story': None,
    }
    return render(request, 'join-story.html', context)


@login_required(login_url=reverse_lazy('signin'))
def write_story_view(request, pk):
    context = {
        'story': None,
    }
    return render(request, 'write-story.html', context)


@login_required(login_url=reverse_lazy('signin'))
def read_story_view(request, pk):
    context = {
        'story': None,
    }
    return render(request, 'read-story.html', context)
