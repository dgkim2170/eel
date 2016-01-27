from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from redactor.widgets import RedactorEditor

from pages.models import Intro, ResearchIntro, ResearchLeft, ResearchRight, \
						Faculty, Collaborator, Student, \
						Contact

# Register your models here.
class DefaultAdmin(admin.ModelAdmin):
	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing'))
	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing'))
	def response_delete(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing'))
admin.site.register(Intro, DefaultAdmin)

class ResearchAdmin(admin.ModelAdmin):
	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ '#research')
	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ '#research')
	def response_delete(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ '#research')
admin.site.register(ResearchLeft, ResearchAdmin)
admin.site.register(ResearchRight, ResearchAdmin)

class ResearchIntroAdminForm(forms.ModelForm):
	text = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = ResearchIntro
		fields = ('text',)
class ResearchIntroAdmin(ResearchAdmin):
	form = ResearchIntroAdminForm
admin.site.register(ResearchIntro, ResearchIntroAdmin)		

class FacultyAdmin(admin.ModelAdmin):
	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ '#faculty')
	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ '#faculty')
	def response_delete(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('landing')+ '#faculty')
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Collaborator, FacultyAdmin)
admin.site.register(Student, FacultyAdmin)

class ContactAdminForm(forms.ModelForm):
	text = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Contact
		fields = ('text', 'address', 'phone', 'email', 'gmap_lat', 'gmap_lng', 'gmap_title')
class ContactAdmin(DefaultAdmin):
	form = ContactAdminForm
admin.site.register(Contact, ContactAdmin)
