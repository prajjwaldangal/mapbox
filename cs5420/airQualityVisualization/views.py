from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('NewMainAQI.html')
    return HttpResponse(template.render())
    # return HttpResponse("Hello, world. You're at the air data visualization index.")	
