from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


def get_default_category() -> int:
    return Category.objects.get(name="Coding").id


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(
        Category, default=get_default_category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)
