# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150713_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='temporary_password_date',
            field=models.DateField(null=True, help_text='If set, it will be assumed that this is a new user or they have opted to reset their password, and this field records the date on which that happened.', blank=True),
        ),
    ]
