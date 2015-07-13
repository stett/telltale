# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, null=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StoryChunk',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', models.CharField(max_length=2400)),
                ('leadin_position', models.IntegerField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('next_chunk', models.ForeignKey(to='stories.StoryChunk', related_name='prev_chunk', blank=True, null=True)),
                ('story', models.ForeignKey(to='stories.Story')),
            ],
        ),
    ]
