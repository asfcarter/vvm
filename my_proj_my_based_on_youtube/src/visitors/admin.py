from django.contrib import admin
from .models import Visitor,Host,Booking


# Register your models here.
admin.site.register(Visitor)
admin.site.register(Host)
admin.site.register(Booking)

