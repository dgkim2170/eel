# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('content', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('position', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'collaborators/')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email_webmaster', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_professor', models.EmailField(blank=True, max_length=254, null=True)),
                ('gmap_lat', models.CharField(blank=True, max_length=20, null=True)),
                ('gmap_lng', models.CharField(blank=True, max_length=20, null=True)),
                ('gmap_title', models.CharField(blank=True, max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('position', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(null=True, upload_to=b'faculty/')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to=b'intro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('small_description', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('code', models.CharField(max_length=255, null=True)),
                ('credit', models.CharField(max_length=10, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to=b'news/')),
                ('published', models.DateField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=b'photo/')),
                ('category', models.CharField(choices=[('category1', 'Category1'), ('category4', 'NEWcategory'), ('category2', 'NEWER')], max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotographCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, null=True)),
                ('category_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('gmap_lat', models.CharField(blank=True, max_length=20, null=True)),
                ('gmap_lng', models.CharField(blank=True, max_length=20, null=True)),
                ('gmap_title', models.CharField(blank=True, max_length=255, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('category', models.CharField(choices=[(b'international', b'International Journals'), (b'domestic', b'Domestic Journals'), (b'book', b'Books')], max_length=255)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('rank', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchIntro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('position', models.CharField(max_length=50, null=True)),
                ('content', models.CharField(max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'students/')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UsefulLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('link', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
