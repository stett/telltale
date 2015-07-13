# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20150713_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='storychunk',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='storychunk',
            name='content',
            field=models.CharField(max_length=2400, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storychunk',
            name='leadin_position',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
