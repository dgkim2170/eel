# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20160224_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='rank',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]