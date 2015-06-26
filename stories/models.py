from django.db import models


class Story(models.Model):
    pass


class StoryChunk(models.Model):
    story = models.ForeignKey(Story)
