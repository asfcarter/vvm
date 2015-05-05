from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

from django.forms import ModelForm


# Create your models here.

class Visitor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    mobile = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    def __unicode__(self):
        return unicode(self.email)

class Host(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    mobile = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Booking(models.Model):
    host = models.ForeignKey(Host)    
    visitor = models.ForeignKey(Visitor)    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    anpr = models.BooleanField()
    greeted = models.BooleanField()
    def __unicode__(self):
        return unicode(self.start_time)
    # Change colour based on time
    def is_past_due(self):
        if (timezone.now()) > self.start_time:
            return True
        return False


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['host', 'visitor', 'start_time', 'end_time']

class Car(models.Model):
    registration = models.CharField(max_length=32)
    host = models.ForeignKey(Host)    
    visitor = models.ForeignKey(Visitor)    
    def __unicode__(self):
        return unicode(self.registration)
