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
    print("[+] Starting service")
    thisSwitch = Switch
    thisSwitch.startService()

    #service functions
    global Service
    Service = service(thisSwitch)
    Service.runThread()

    status = thisSwitch.retStatus()
    html = loader.get_template('frontend/index.html')
    backupCards = backupFolder.objects.all()
    context = {'status': status.upper(), 'backupCards': backupCards}
    return HttpResponse(html.render(context, request))

def stopService(request):
    print("[+] Stopping service")
    thisSwitch = Switch
    thisSwitch.stopService()
    status = thisSwitch.retStatus()
    html = loader.get_template('frontend/index.html')
    backupCards = backupFolder.objects.all()
    context = {'status': status.upper(), 'backupCards': backupCards}
    return HttpResponse(html.render(context, request))

def home(request):
    thisSwitch = Switch
    status = thisSwitch.retStatus()
    html = loader.get_template('frontend/index.html')
    backupCards = backupFolder.objects.all()
    context = {'status': status.upper(), 'backupCards': backupCards}
    return HttpResponse(html.render(context, request))

def addcard(request):
    thisSwitch = Switch
    status = ""
    status = thisSwitch.retStatus()

    lastid = backupFolder.objects.all().order_by('-id')[0].id

    #/addcard?name=yo&source=yo&dest=yo
    newcard = backupFolder()
    newcard.id = lastid+1
    newcard.name = request.GET['name']
    newcard.path = request.GET['source']
    newcard.backupPath = request.GET['dest']

    newcard.save()

    html = loader.get_template('frontend/index.html')
    backupCards = backupFolder.objects.all()
    context = {'status': status.upper(), 'backupCards': backupCards}
    return HttpResponse(html.render(context, request))
