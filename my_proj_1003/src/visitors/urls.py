from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from visitors.models import Visitor
from visitors import views

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Visitor, context_object_name="visitor_list", ), name='index'),
    url(r'^bbaa/$', views.IndexView.as_view(), name='index'),
    url(r'^lllist/$', views.DetailView.as_view()), 
    url(r'^list/$', views.DetailView.as_view()), 
)
