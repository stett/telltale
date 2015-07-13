# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20150713_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='story',
            name='authors',
            field=models.ManyToManyField(related_name='stories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='storychunk',
            name='leadin',
            field=models.CharField(max_length=400, blank=True, null=True),
        ),
    ]
