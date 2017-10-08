from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns =[
    url(r'^$',views.login),
    url(r'^home/',views.home),
    url(r'^on/',views.runService),
    url(r'^off/',views.stopService),
    url(r'^addcard/',views.addcard),
]
