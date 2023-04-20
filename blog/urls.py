from django.urls import path
from .views import PostListView
from .views import PostDetailView
from .views import PostCreateView
from .views import PostUpdateView
from .views import PostDeleteView
from .views import UserPostListView
from . import views

# Mapping for the urls
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='post-user'),
    path('about/', views.about, name='blog-about'),
]