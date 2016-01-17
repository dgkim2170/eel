# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('position', models.CharField(max_length=50, null=True)),
                ('content', models.CharField(max_length=255, null=True)),
                ('photo', models.ImageField(null=True, upload_to='faculty/')),
            ],
        ),
    ]
