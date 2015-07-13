from django.db import models
from django.conf import settings


class Story(models.Model):
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    manager = models.ForeignKey('users.User')

    class Meta:
        app_label = 'stories'


class StoryChunk(models.Model):
    story = models.ForeignKey('stories.Story')
    author = models.ForeignKey('users.User')
    prev_chunk = models.OneToOneField(
        'stories.StoryChunk',
        related_name='next_chunk',
        null=True,
        blank=True)
    content = models.CharField(
        max_length=(settings.MAX_STORY_CHUNK_SIZE +
                    settings.MAX_STORY_LEADIN_SIZE),
        null=True,
        blank=True)
    leadin_position = models.IntegerField(
        null=True,
        blank=True)

    class Meta:
        app_label = 'stories'
