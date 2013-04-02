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

def characterpage(request, ):

	template = get_template('characterpage.html')
	variables = Context({
		'titlehead': 'PNJ',
		'pagetitle': 'Prova',
		'contentbody': 'Ed'
	})
	
	output = template.render(variables)
	return HttpResponse(output)

def housepage(request, ):

	template = get_template('housepage.html')
	variables = Context({
		'titlehead': 'House',
		'pagetitle': 'Prova',
		'contentbody': 'Lannister'
	})
	
	output = template.render(variables)
	return HttpResponse(output)

def placepage(request, ):

	template = get_template('placepage.html')
	variables = Context({
		'titlehead': 'Place',
		'pagetitle': 'Prova',
		'contentbody': 'Winterfell'
	})
	
	output = template.render(variables)
	return HttpResponse(output)
