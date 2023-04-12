from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Paths to the suffix

def home(request):
    return HttpResponse('<h1>Home</h1>')


def blog(request):
    return HttpResponse('<h1>Blog</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')