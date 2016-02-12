from django.shortcuts import render

from pages.models import Intro, ResearchIntro, Research, Project, \
						Faculty, Collaborator, Student, Alumnus, Publication, \
						Lecture, UsefulLink, Calender, \
						PhotographCategory, Photograph, News, Contact

# Create your views here.
def index(request):
	context = {}
	context['intro'] = Intro.objects.latest('updated')
	context['researchintro'] = ResearchIntro.objects.latest('made')
	context['research'] = Research.objects.all()
	context['currentprojects'] = Project.objects.filter(visible=True)
	# context['researchright'] = ResearchRight.objects.all()
	context['faculty'] = Faculty.objects.all()
	context['collaborators'] = Collaborator.objects.all()
	context['students'] = Student.objects.all()
	context['alumni'] = Alumnus.objects.all()
	context['international_featured'] = Publication.objects.filter(featured=True).filter(category='international')
	context['domestic_featured'] = Publication.objects.filter(featured=True).filter(category='domestic')
	context['book_featured'] = Publication.objects.filter(featured=True).filter(category='book')
	context['international'] = Publication.objects.filter(featured=False).filter(category='international')
	context['domestic'] = Publication.objects.filter(featured=False).filter(category='domestic')
	context['book'] = Publication.objects.filter(featured=False).filter(category='book')
	context['lectures'] = Lecture.objects.all()
	context['usefullinks'] = UsefulLink.objects.all()
	calender = Calender.objects.all()
	context['calender'] = [event.get_obj() for event in calender]
	context['photocategories'] = PhotographCategory.objects.all()
	context['photographs'] = Photograph.objects.all()
	context['news'] = News.objects.all()
	context['contact'] = Contact.objects.latest('updated')
	return render(request, 'pages/index.html', context)