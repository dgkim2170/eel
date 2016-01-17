from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from pages.models import Intro, ResearchLeft, ResearchRight, Faculty, \
						Contact

# Register your models here.
class DefaultAdmin(admin.ModelAdmin):
	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault'))
	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault'))
	def response_delete(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault'))

class ResearchAdmin(admin.ModelAdmin):
	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault')+ '#research')
	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault')+ '#research')
	def response_delete(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault')+ '#research')

class FacultyAdmin(admin.ModelAdmin):
	def response_change(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault')+ '#faculty')
	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault')+ '#faculty')
	def response_delete(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect(reverse('homedefault')+ '#faculty')

admin.site.register(Intro, DefaultAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(ResearchLeft, ResearchAdmin)
admin.site.register(ResearchRight, ResearchAdmin)
admin.site.register(Contact)