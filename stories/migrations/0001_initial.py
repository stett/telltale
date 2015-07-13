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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(blank=True, null=True, max_length=255)),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'stories',
            },
        ),
        migrations.CreateModel(
            name='StoryChunk',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=2000)),
                ('leadin', models.CharField(max_length=400)),
                ('published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('next_chunk', models.OneToOneField(blank=True, null=True, to='stories.StoryChunk', related_name='prev_chunk')),
                ('story', models.ForeignKey(blank=True, null=True, to='stories.Story', related_name='chunks')),
            ],
        ),
    ]
