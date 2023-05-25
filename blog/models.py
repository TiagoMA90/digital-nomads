from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.validators import MaxLengthValidator


# Post Model
class Post(models.Model):                                                          # The Post should displays and allows the following:
    title = models.CharField(max_length=150)                                       # Title field for 150 characters
    content = models.TextField(validators=[MaxLengthValidator(5000)])              # Text field set for 5k characters
    date_posted = models.DateTimeField(default=timezone.now)                       # Time Stamp for the default Time Zone
    author = models.ForeignKey(User, on_delete=models.CASCADE)                     # Username, if User gets delete so are its Posts
    likes = models.ManyToManyField(User, related_name='posts')                     # Likes in relation to a Post

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()


# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)    # Comment in relation to a Post
    body = models.TextField()                                                            # Body of the Comment
    date_commented = models.DateTimeField(auto_now_add=True)                             # Time Stamp for the default Time Zone
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Username, if User gets delete so are its Posts

    def __str__(self):
        return self.post.title
        return f"{self.author.username} - {self.post.title}"