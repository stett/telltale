# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_story_current_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='max_chunks',
            field=models.IntegerField(default=10),
        ),
    ]
