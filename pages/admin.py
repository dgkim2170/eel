from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from redactor.widgets import RedactorEditor

from pages.models import Intro, ResearchIntro, Research, \
						Faculty, Collaborator, Student, Publication, \
						Lecture, UsefulLink, Calender, \
						PhotographCategory, Photograph, News, Contact

# Register your models here.
class DefaultAdmin(admin.ModelAdmin):
	urladd = ''
	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ self.urladd)
	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ self.urladd)
	def response_delete(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ self.urladd)

class IntroAdminForm(forms.ModelForm):
	content = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Intro
		fields = ('title', 'content', 'image')
class IntroAdmin(DefaultAdmin):
	form = IntroAdminForm
admin.site.register(Intro, IntroAdmin)

class ResearchAdminForm(forms.ModelForm):
	content = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Research
		fields = ('title', 'icon', 'content')
class ResearchAdmin(DefaultAdmin):
	urladd = '#research'
	form = ResearchAdminForm
admin.site.register(Research, ResearchAdmin)
# admin.site.register(ResearchRight, ResearchAdmin)

class ResearchIntroAdminForm(forms.ModelForm):
	text = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = ResearchIntro
		fields = ('text',)
class ResearchIntroAdmin(ResearchAdmin):
	form = ResearchIntroAdminForm
admin.site.register(ResearchIntro, ResearchIntroAdmin)		

class FacultyAdmin(DefaultAdmin):
	urladd = '#faculty'
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Collaborator, FacultyAdmin)
admin.site.register(Student, FacultyAdmin)

class PublicationAdminForm(forms.ModelForm):
	description = forms.CharField(widget=RedactorEditor())
	class Meta:
		model = Publication
		exclude = ()
class PublicationAdmin(DefaultAdmin):
	urladd = '#publications'
	form = PublicationAdminForm
admin.site.register(Publication, PublicationAdmin)

class LectureAdminForm(forms.ModelForm):
	description = forms.CharField(widget=RedactorEditor())
	class Meta:
		model = Lecture
		exclude = ()
class LectureAdmin(DefaultAdmin):
	urladd = '#education'
	form = LectureAdminForm
admin.site.register(Lecture, LectureAdmin)

class UsefullinkAdminForm(forms.ModelForm):
	description = forms.CharField(widget=RedactorEditor())
	class Meta:
		model = UsefulLink
		exclude = ()
class UsefullinkAdmin(DefaultAdmin):
	urladd = '#education'
	form = UsefullinkAdminForm
admin.site.register(UsefulLink, UsefullinkAdmin)

admin.site.register(Calender)

class PhotoAdminForm(forms.ModelForm):
	class Meta:
		model = Photograph
		# fields = ['category']
		fields = ('image', 'category', 'title', 'description', 'date')
	def __init__(self, *args, **kwargs):
		super(PhotoAdminForm, self).__init__(*args, **kwargs)
		CATEGORIES = [cat.get_tuple() for cat in PhotographCategory.objects.all()]
		self.fields['category'].choices = CATEGORIES
class PhotoAdmin(admin.ModelAdmin):
	urladd = '#photographs'
	# def formfield_for_choice_field(self, db_field, request, **kwargs):
	# 	if db_field.name == 'category':
	# 		kwargs['choices'] = [cat.get_tuple() for cat in PhotographCategory.objects.all()]
	# 	return super(PhotoAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)
	form = PhotoAdminForm
admin.site.register(PhotographCategory)
admin.site.register(Photograph,PhotoAdmin)

class NewsAdminForm(forms.ModelForm):
	description = forms.CharField(widget=RedactorEditor())
	class Meta:
		model = News
		exclude = ()
class NewsAdmin(DefaultAdmin):
	urladd = '#news'
	form = NewsAdminForm
admin.site.register(News, NewsAdmin)

class ContactAdminForm(forms.ModelForm):
	text = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Contact
		fields = ('text', 'address', 'phone', 'email', 'gmap_lat', 'gmap_lng', 'gmap_title')
class ContactAdmin(DefaultAdmin):
	urladd = '#contact'
	form = ContactAdminForm
admin.site.register(Contact, ContactAdmin)
