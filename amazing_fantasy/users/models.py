from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    country = models.CharField(max_length=40)


class Note(models.Model):
    title = models.CharField(max_length=40)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        ordering = ['-pub_date']
