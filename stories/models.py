from django.db import models
from django.conf import settings


class Story(models.Model):
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    manager = models.ForeignKey('users.User', related_name='managed_stories')
    authors = models.ManyToManyField('users.User')

    class Meta:
        app_label = 'stories'
        verbose_name_plural = 'stories'

    def __str__(self):
        return "%s by %s" % (self.get_title(), self.manager)

    def get_title(self):
        return self.title or "Untitled"

    def get_first_chunk(self):
        if self.chunks.count() > 0:
            return self.chunks.get(prev_chunk__isnull=True)
        return None

    def get_last_chunk(self):
        if self.chunks.count() > 0:
            return self.chunks.get(next_chunk__isnull=True)
        return None


class StoryChunk(models.Model):
    story = models.ForeignKey(
        'stories.Story',
        related_name='chunks',
        null=True,
        blank=True)
    author = models.ForeignKey(
        'users.User',
        null=True,
        blank=True)
    next_chunk = models.OneToOneField(
        'stories.StoryChunk',
        related_name='prev_chunk',
        null=True,
        blank=True)
    content = models.CharField(max_length=settings.MAX_STORY_CHUNK_SIZE)
    leadin = models.CharField(max_length=settings.MAX_STORY_LEADIN_SIZE)
    published = models.BooleanField(default=False)

    class Meta:
        app_label = 'stories'
