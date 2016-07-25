from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse({"name":"lifeng", "age":33})

def detail(request):
    return HttpResponse("Detail")