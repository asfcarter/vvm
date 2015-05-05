from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from visitors.models import Visitor, Booking
from visitors import views
from visitors.views import VisitorDetailView

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Visitor, context_object_name="visitor_list", ), name='index'),
    url(r'^bookings/$', ListView.as_view(model=Booking, context_object_name="booking_list", ), name='booking'),
    url(r'^email/$', ListView.as_view(model=Booking, context_object_name="booking_list", ), name='email'),
    url(r'^(?P<pk>\d+)/$', VisitorDetailView.as_view(), name='visitor-detail'),
    #url(r'^(?P<slug>[-_\w]+)/$', VisitorDetailView.as_view(), name='visitor-detail'),
    url(r'^bookings/booking_table_update/$', 'visitors.views.booking_table_update'),
    url(r'^bookings/send_host_request/$', 'visitors.views.send_host_request'    ),
    url(r'^bookings/update_anpr/$', 'visitors.views.update_anpr'    ),
    url(r'^bookings/update_anpr/$', 'visitors.views.update_anpr'    ),
    url(r'^add_booking/$', 'visitors.views.add_booking'             ),
)
