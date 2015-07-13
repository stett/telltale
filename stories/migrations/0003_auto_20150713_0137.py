# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storychunk',
            name='next_chunk',
        ),
        migrations.AddField(
            model_name='storychunk',
            name='prev_chunk',
            field=models.OneToOneField(to='stories.StoryChunk', null=True, blank=True, related_name='next_chunk'),
        ),
        migrations.AlterField(
            model_name='storychunk',
            name='content',
            field=models.CharField(blank=True, null=True, max_length=2400),
        ),
        migrations.AlterField(
            model_name='storychunk',
            name='leadin_position',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
