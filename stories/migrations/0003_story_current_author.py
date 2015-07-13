# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0002_auto_20150713_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='current_author',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='current_stories', null=True),
        ),
    ]
