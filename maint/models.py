import datetime
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Work.Status.PUBLISHED)


class Work(models.Model):
    '''
    The basics:
    '''
    class Status(models.TextChoices):
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')

    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maint_work') #  specify the name of the reverse relationship, from User to Work. 
    code = models.CharField(max_length=101, default='XX-XX:XXXX')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # returns the current datetime in a timezone-aware format
    created = models.DateTimeField(auto_now_add=True) #  the date will be saved automatically when creating an object
    updated = models.DateTimeField(auto_now=True) # the date will be updated automatically when saving an object.
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ['code']
        indexes = [
            models.Index(fields=['code']), # Creates an index (B-Tree) in the database. This will improve performance for queries filtering or ordering results by this field.
        ]



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('maint:work-detail', args=[self.slug])
    
    # 
    @property
    def short_description(self):
        return self.content if len(self.content) < 35 else (self.content[:33] + '..')
