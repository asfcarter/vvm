import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Visitor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32,null=True)
    mobile = models.CharField(max_length=32,null=True)
    company = models.CharField(max_length=32,null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.email

class Host(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32,null=True)
    mobile = models.CharField(max_length=32,null=True)
    company = models.CharField(max_length=32,null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.email

class Booking(models.Model):
    host = models.ForeignKey(Host)
    visitor = models.ForeignKey(Visitor,null=True)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.start_time
