from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('NewMainAQI.html')
    # template = loader.get_template('simple.html')
    return HttpResponse(template.render())
