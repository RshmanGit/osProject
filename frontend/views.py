from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from switch import switch
from service import service
import urllib


# Create your views here.

global Switch
global Service

def login(request):
    global Switch
    Switch = switch()
    html = loader.get_template('frontend/index.html')
    backupCards = backupFolder.objects.all()
    context = {'backupCards': backupCards}
    return HttpResponse(html.render(context, request))

def runService(request):
    thisSwitch = Switch
    thisSwitch.startService()

    #service functions
    global Service
    Service = service(thisSwitch)
    Service.runThread()

    status = thisSwitch.retStatus()
    html = loader.get_template('frontend/index.html')
    backupCards = backupFolder.objects.all()
    context = {'status': status.upper(), 'backupCards': bcakupCards}
    return HttpResponse(html.render(context, request))

def stopService(request):
    thisSwitch = Switch
    thisSwitch.stopService()
    status = thisSwitch.retStatus()
    html = loader.get_template('frontend/index.html')
    backupCards = backupFolder.objects.all()
    context = {'status': status.upper(), 'backupCards': bcakupCards}
    return HttpResponse(html.render(context, request))

def home(request):
    thisSwitch = Switch
    status = thisSwitch.retStatus()
    html = loader.get_template('frontend/index.html')
    backupCards = backupFolder.objects.all()
    context = {'status': status.upper(), 'backupCards': bcakupCards}
    return HttpResponse(html.render(context, request))
