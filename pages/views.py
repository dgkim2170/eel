from django.shortcuts import render

from pages.models import Intro, ResearchLeft, ResearchRight, Faculty, \
						Contact

# Create your views here.
def index(request):
	context = {}
	context['intro'] = Intro.objects.latest('updated')
	context['researchleft'] = ResearchLeft.objects.all()
	context['researchright'] = ResearchRight.objects.all()
	context['faculty'] = Faculty.objects.all()
	context['contact'] = Contact.objects.latest('updated')
	return render(request, 'pages/index.html', context)