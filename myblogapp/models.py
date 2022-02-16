from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


def get_default_category() -> int:
    return Category.objects.get(name="Coding").id



class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, default=get_default_category, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=200, default="NO SNIPPET HERE!")
    likes = models.ManyToManyField(User, related_name="blog_likes")

    def count_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)




class Profile(models.Model):
    user = models.OneToOneField(User,  null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(null=True,blank=True,max_length=255)
    fb_url = models.CharField(null=True,blank=True,max_length=255)
    instagram_url = models.CharField(null=True,blank=True,max_length=255)
    linkedIn_url = models.CharField(null=True,blank=True,max_length=255)
    github_url = models.CharField(null=True,blank=True,max_length=255)

    def __str__(self) -> str:
        return str(self.user)
