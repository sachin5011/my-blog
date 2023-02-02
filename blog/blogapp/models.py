from django.db import models
from datetime import *
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title


class About(models.Model):
    abt_title = models.CharField(max_length=200)
    abt_data = models.TextField()


    def __str__(self):
        return 'about_title'



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=14)
    message = models.TextField()


    def __str__(self):
        return self.name
        