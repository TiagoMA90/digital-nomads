from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=150)                    # Title field for 150 characters
    content = models.TextField()                                # Text field
    date_posted = models.DateTimeField(default=timezone.now)     # Time Stamp for the defaults Time Zone
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User if User gets delete, so are its Posts

    def __str__(self):
        return self.title