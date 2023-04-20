from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

# Routing for the urls
def home(request):
    context= {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html')


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    descending_order = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
