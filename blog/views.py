from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

# Routing for the urls
def home(request):
    context= {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
