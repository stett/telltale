# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20150713_0242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'stories'},
        ),
        migrations.RemoveField(
            model_name='storychunk',
            name='prev_chunk',
        ),
        migrations.AddField(
            model_name='storychunk',
            name='next_chunk',
            field=models.OneToOneField(blank=True, null=True, to='stories.StoryChunk', related_name='prev_chunk'),
        ),
    ]
