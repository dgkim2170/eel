# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_news_featured'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
