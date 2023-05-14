from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Post Model
class Post(models.Model):
    title = models.CharField(max_length=150)                    # Title field for 150 characters
    content = RichTextField(blank=True, null=True)                                # Text field
    date_posted = models.DateTimeField(default=timezone.now)    # Time Stamp for the defaults Time Zone
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User if User gets delete, so are its Posts
    likes = models.ManyToManyField(User, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()


# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.post.title
        return f"{self.author.username} - {self.post.title}"