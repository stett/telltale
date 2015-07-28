# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_auto_20150713_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='num_chunks',
            field=models.IntegerField(default=4),
        ),
    ]
