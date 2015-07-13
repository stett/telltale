# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_story_max_chunks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='max_chunks',
            new_name='num_chunks',
        ),
    ]
