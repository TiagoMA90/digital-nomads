from django.shortcuts import render
from django.shortcuts import get_object_or_404


# Routing for the urls
def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
