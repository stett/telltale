from stories.models import Story


def top_story(request):
    """
    Puts the current user's "top story", a selected story that they have to
    work on, into the context.
    """
    if request.user and request.user.is_authenticated():
        return {
            'top_story': Story.objects.filter(
                finished=False,
                current_author=request.user).order_by('?').first()}
    return {}
