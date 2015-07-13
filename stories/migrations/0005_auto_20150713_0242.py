# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20150713_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storychunk',
            name='story',
            field=models.ForeignKey(related_name='chunks', to='stories.Story'),
        ),
    ]
