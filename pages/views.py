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
	context['research'] = Research.objects.all().order_by('rank')
	context['currentprojects'] = Project.objects.filter(visible=True).order_by('rank')
	# context['researchright'] = ResearchRight.objects.all()
	context['prof'] = Faculty.objects.latest('updated')
	context['collaborators'] = Collaborator.objects.all().order_by('rank')
	context['students'] = Student.objects.all().order_by('rank')
	context['alumni'] = Alumnus.objects.all()
	context['international_featured'] = Publication.objects.filter(featured=True).filter(category='international').order_by('rank')
	context['domestic_featured'] = Publication.objects.filter(featured=True).filter(category='domestic').order_by('rank')
	context['book_featured'] = Publication.objects.filter(featured=True).filter(category='book').order_by('rank')
	context['international'] = Publication.objects.filter(featured=False).filter(category='international').order_by('rank')
	context['domestic'] = Publication.objects.filter(featured=False).filter(category='domestic').order_by('rank')
	context['book'] = Publication.objects.filter(featured=False).filter(category='book').order_by('rank')
	context['lectures'] = Lecture.objects.all().order_by('rank')
	context['usefullinks'] = UsefulLink.objects.all().order_by('rank')
	calender = Calender.objects.all()
	context['calender'] = [event.get_obj() for event in calender]
	context['photocategories'] = PhotographCategory.objects.all()
	context['photographs'] = Photograph.objects.all()
	context['news'] = News.objects.all()
	context['contact'] = Contact.objects.latest('updated')
	return render(request, 'pages/index.html', context)