from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Catergory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)
