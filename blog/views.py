from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Blog Home")

def about(request):
    return HttpResponse("Hello Blog About")
