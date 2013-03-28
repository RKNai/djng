# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'GoT Database',
		'pagetitle': 'Welcome to the database of GoT',
		'contentbody': 'Killing Starks since 1996 (Warning! Can content major Spoilers!)'
	})
	
	output = template.render(variables)
	return HttpResponse(output)
