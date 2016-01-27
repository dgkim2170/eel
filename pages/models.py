from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Intro(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='intro', null=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '['+str(self.updated)+']'+ self.title

class ResearchIntro(models.Model):
	text = models.CharField(max_length=255, blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return 'Research Intro Text'

class Research(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	icon = models.CharField(max_length=50, blank=True, null=True)
	content = models.TextField(blank=True, null=True)

	class Meta:
		abstract = True

class ResearchLeft(Research):
	def __unicode__(self):
		return '[left]'+ self.title

class ResearchRight(Research):
	def __unicode__(self):
		return '[right]'+ self.title

class Faculty(models.Model):
	name = models.CharField(max_length=50, null=True)
	position = models.CharField(max_length=50, null=True)
	content = models.CharField(max_length=255, null=True)
	photo = models.ImageField(upload_to='faculty/', null=True)
	email = models.EmailField(null=True)

	def __unicode__(self):
		return self.name

class Collaborator(models.Model):
	name = models.CharField(max_length=50, null=True)
	position = models.CharField(max_length=50, null=True)
	content = models.CharField(max_length=255, null=True)
	photo = models.ImageField(upload_to='collaborators/', null=True)
	email = models.EmailField(null=True)

	def __unicode__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=50, null=True)
	position = models.CharField(max_length=50, null=True)
	content = models.CharField(max_length=255, null=True)
	photo = models.ImageField(upload_to='students/', null=True)
	email = models.EmailField(null=True)

	def __unicode__(self):
		return self.name

class Contact(models.Model):
	text = models.CharField(max_length=1000, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)
	phone = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	gmap_lat = models.CharField(max_length=20, blank=True, null=True)
	gmap_lng = models.CharField(max_length=20, blank=True, null=True)
	gmap_title = models.CharField(max_length=255, blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '['+str(self.updated)+']Contact info'