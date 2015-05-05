from django.contrib import admin

# Register your models here.

from visitors.models import Visitor, Host, Car, Booking

admin.site.register(Visitor)
admin.site.register(Host)
admin.site.register(Car)
admin.site.register(Booking)
