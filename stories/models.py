from django.db import models
from django.db.models import Q
from django.conf import settings


class Story(models.Model):
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    num_chunks = models.IntegerField(default=settings.STORY_CHUNK_NUMBER)
    manager = models.ForeignKey(
        'users.User',
        related_name='managed_stories')
    authors = models.ManyToManyField(
        'users.User',
        related_name='stories')
    current_author = models.ForeignKey(
        'users.User',
        related_name='current_stories',
        null=True,
        blank=True)
    finished = models.BooleanField(default=False)

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

    def get_progress(self):
        return int(100 * float(self.chunks.count()) / float(self.num_chunks))

    def get_concatenation(self):
        cat = ''
        chunk = self.get_first_chunk()
        while chunk:
            cat = '%s%s %s ' % (cat, chunk.content, chunk.leadin)
            chunk = chunk.next_chunk
        return cat

    def get_preview(self):
        cat = self.get_concatenation()
        if len(cat) > settings.STORY_PREVIEW_SIZE:
            cat = "%s..." % cat[:(settings.STORY_PREVIEW_SIZE-3)]
        return cat

    def update_current_author(self):

        # Find the N most recent authors which we want to exclude, and make a
        # queryset of all of them.
        q = Q()
        chunk = self.get_last_chunk()
        num_authors_excluded = 0
        while chunk and num_authors_excluded < settings.STORY_AUTHOR_SPACING:
            q = q | Q(pk=chunk.author.pk)
            chunk = self.chunks.filter(next_chunk=chunk).first()
            num_authors_excluded += 1

        # Get a set of all authors for this story who are not excluded. If it's
        # not an empty list, pick an author from it. Otherwise, pick the author
        # of the first chunk, or else a random author.
        authors = self.authors.filter(~q)
        if authors.count() > 0:
            self.current_author = authors.order_by('?').first()
        elif self.chunks.count() > 0:
            self.current_author = self.get_first_chunk().author
        else:
            self.current_author = self.authors.order_by('?').first()

        # Save the new thing
        self.save()

    def mark_finished(self):
        self.finished = True
        self.save()


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
    content = models.TextField(max_length=settings.MAX_STORY_CHUNK_SIZE)
    leadin = models.TextField(
        max_length=settings.MAX_STORY_LEADIN_SIZE,
        null=True,
        blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        app_label = 'stories'

    def __str__(self):
        return '...%s...' % self.content[:50]
