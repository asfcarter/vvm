from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views
from visitors.views import HelloTemplate

#from django.contrib import visitors

urlpatterns = patterns(
    '',
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'visitors.views.hello'),
    url(r'^hello_template/', 'visitors.views.hello_template'),        
    url(r'^hello_template_class/', HelloTemplate.as_view()),        
    url(r'^hello_template_simple/', 'visitors.views.hello_template_simple'),        
    url(r'^visitors/', include('visitors.urls')),
)

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
