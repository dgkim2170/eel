# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20160130_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
