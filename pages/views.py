from django.shortcuts import render

from pages.models import Intro, ResearchIntro, Research, \
						Faculty, Collaborator, Student, Publication, \
						Lecture, UsefulLink, Calender, \
						PhotographCategory, Photograph, News, Contact

# Create your views here.
def index(request):
	context = {}
	context['intro'] = Intro.objects.latest('updated')
	context['researchintro'] = ResearchIntro.objects.latest('made')
	context['research'] = Research.objects.all()
	# context['researchright'] = ResearchRight.objects.all()
	context['faculty'] = Faculty.objects.all()
	context['collaborators'] = Collaborator.objects.all()
	context['students'] = Student.objects.all()
	context['publications'] = Publication.objects.all()
	context['lectures'] = Lecture.objects.all()
	context['usefullinks'] = UsefulLink.objects.all()
	calender = Calender.objects.all()
	context['calender'] = [event.get_obj() for event in calender]
	context['photocategories'] = PhotographCategory.objects.all()
	context['photographs'] = Photograph.objects.all()
	context['news'] = News.objects.all()
	context['contact'] = Contact.objects.latest('updated')
	return render(request, 'pages/index.html', context)