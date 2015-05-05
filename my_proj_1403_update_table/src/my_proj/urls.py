from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import visitors.urls
import profiles.urls
import accounts.urls


from . import views

#urlpatterns = patterns('',
#        url(r'^Vodafone/', include(patterns('wiki.views',
#            url(r'^history/$', 'history'),
#            url(r'^edit/$', 'edit'),
#            url(r'^discuss/$', 'discuss'),
#            url(r'^permissions/$', 'permissions'),
#            ))),
#        )

urlpatterns = patterns('',
        url(r'^Vodafone/', 
            include([
                url(r'^$', views.HomePage.as_view(), name='home'),
                url(r'^about/$', views.AboutPage.as_view(), name='about'),
                url(r'visitors/', include(visitors.urls, namespace='visitors')),
                url(r'^users/', include(profiles.urls, namespace='profiles')),
                url(r'^admin/', include(admin.site.urls)),
                url(r'^', include(accounts.urls, namespace='accounts')),
                ])),
            )



# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
