from django.urls import path
from .views import PostListView
from . import views

# Mapping for the urls
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]