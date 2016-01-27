from django.shortcuts import render

from pages.models import Intro, ResearchIntro, ResearchLeft, ResearchRight, \
						Faculty, Collaborator, Student, \
						Contact

# Create your views here.
def index(request):
	context = {}
	context['intro'] = Intro.objects.latest('updated')
	context['researchintro'] = ResearchIntro.objects.latest('made')
	context['researchleft'] = ResearchLeft.objects.all()
	context['researchright'] = ResearchRight.objects.all()
	context['faculty'] = Faculty.objects.all()
	context['collaborators'] = Collaborator.objects.all()
	context['students'] = Student.objects.all()
	context['contact'] = Contact.objects.latest('updated')
	return render(request, 'pages/index.html', context)