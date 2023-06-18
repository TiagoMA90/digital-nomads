# Imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import Post
from .models import Comment
from .models import Contact
from users.models import Profile
from .forms import ContactForm


# Routing for the urls
# Home Views
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html')


# About Views
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# Guild Views
def guild(request):
    profiles = Profile.objects.all()
    return render(request, 'blog/guild.html', {'profiles':profiles})


# Contact Views
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/contact_success.html')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'blog/contact.html', context)


# 404
def error_404(request, exception):
    return render(request, '404.html', status=404)


# Search Bar
def search(request):
    if request.method == "POST":
        searches = request.POST.get('searches')
        results = Post.objects.filter(
            Q(content__icontains=searches) |
            Q(author__username__icontains=searches) |
            Q(title__icontains=searches)
            )

        return render(
            request, 'blog/search.html', (
                {'searches': searches, 'results': results}))
    else:
        return render(request, 'blog/search.html', {})


# Post View
class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        click = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = click.total_likes()
        liked = False

        if click.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked

        return context


# C R U D
# Create View
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    login_url = "/login/"
    redirect_field_name = "/home/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update View
class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    login_url = "/login/"
    redirect_field_name = "/home/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# Delete View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# Post View
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6


# User Post Views
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/post_user.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)


# Comment View
class PostCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blog/post_comment.html'
    login_url = "/login/"
    redirect_field_name = "/home/"
    fields = ['body']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = "/"


# Like Views
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    # if the post is liked by the registered user Unlike/Remove the Like
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    # otherwise Like/Add a Like
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))