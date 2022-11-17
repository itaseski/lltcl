import datetime
from django.db import models

from django.utils import timezone


class Work(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # returns the current datetime in a timezone-aware format
    created = models.DateTimeField(auto_now_add=True) #  the date will be saved automatically when creating an object
    updated = models.DateTimeField(auto_now=True) # the date will be updated automatically when saving an object.



    def __str__(self):
        return self.title
