from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #auto_now_add=True could be used as an alternative, but means the time is fixed to whatever the very first one was
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete means the Post is deleted if the User is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
