# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 05:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProject', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 11, 21, 49, 314424)),
        ),
    ]
