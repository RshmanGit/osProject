from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *


# Create your views here.
def login(request):
    html = loader.get_template('frontend/index.html')
    context = {}
    return HttpResponse(html.render(context, request))
