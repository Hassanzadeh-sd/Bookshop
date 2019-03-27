from django.shortcuts import render
from django.http import HttpResponse

def listview(request):
    return HttpResponse("testt")

def detail(request,pk):
    return HttpResponse("booook" + str(pk))