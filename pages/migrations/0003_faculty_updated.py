# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 04:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_faculty_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 2, 20, 4, 22, 29, 292922, tzinfo=utc)),
            preserve_default=False,
        ),
    ]