from datetime import datetime

from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):

    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = News.Status.Publish)




class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DR', "Draft"
        Publish = 'PB', "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(auto_now_add=datetime.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)


    objects = models.Manager()
    published = PublishManager()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_time']


class Contact(models.Model):

    user = models.CharField(max_length=150)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.user


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)



    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.body


