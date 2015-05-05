from django.db import models

# Create your models here.

class Visitor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    llast_name = models.CharField(max_length=32)
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
        return unicode(self.email)
    
class Booking(models.Model):
    host = models.ForeignKey(Host)    
    visitor = models.ForeignKey(Visitor)    
    start_time = models.DateField()
    end_time = models.DateField()
    def __unicode__(self):
        return unicode(self.start_time)

class Car(models.Model):
    registration = models.CharField(max_length=32)
    host = models.ForeignKey(Host)    
    visitor = models.ForeignKey(Visitor)    
    def __unicode__(self):
        return unicode(self.registration)
