# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20160229_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, default=b'media/students/eel.jpg', null=True, upload_to=b'students/'),
        ),
    ]