from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def detail(request):
    return HttpResponse("Detail")