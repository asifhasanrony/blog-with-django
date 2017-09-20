from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"id": self.id})


class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.comment
