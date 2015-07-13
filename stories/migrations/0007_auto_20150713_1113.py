# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_auto_20150713_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storychunk',
            name='content',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='storychunk',
            name='leadin',
            field=models.TextField(null=True, max_length=400, blank=True),
        ),
    ]
