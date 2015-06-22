from django.shortcuts import render


def list_stories_view(request):
    context = {
        'stories': [],
    }
    return render(request, 'list-stories.html', context)


def new_story_view(request):
    context = {
        'form': None,
    }
    return render(request, 'new-story.html', context)


def join_story_view(request, pk):
    context = {
        'story': None,
    }
    return render(request, 'join-story.html', context)


def write_story_view(request, pk):
    context = {
        'story': None,
    }
    return render(request, 'write-story.html', context)


def read_story_view(request, pk):
    context = {
        'story': None,
    }
    return render(request, 'read-story.html', context)
