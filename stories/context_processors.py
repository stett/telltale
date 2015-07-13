from stories.models import Story


def top_story(request):
    """
    Puts the current user's "top story", a selected story that they have to
    work on, into the context.
    """
    context = {
        'top_story': Story.objects.filter(authors=request.user).order_by('?').first(),
    }
    return context
