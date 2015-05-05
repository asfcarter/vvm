from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^all/', 'visitors.views.visitors'),        
    url(r'^get/(?P<visitor_id>\d+)/$', 'visitors.views.visitor'),
)
