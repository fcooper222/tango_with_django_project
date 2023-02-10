from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<a href=\"about/\">here is the about page<a/>")


def about(request):
    return HttpResponse('Rango says here is the about page.')
