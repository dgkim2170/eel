# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 04:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='updated',
        ),
    ]