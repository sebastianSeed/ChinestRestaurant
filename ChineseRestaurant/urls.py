from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ChineseRestaurant.views.home', name='home'),
    # url(r'^ChinestRestaurant/', include('ChinestRestaurant.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Include each apps URLS here
    url(r'^roster/', include('staffRosterApp.urls')),
    url(r'^menu/', include('menuApp.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Note the above line is a workaround for dev
# In porduction media url should be an apache or similar url
# eg put all your files under /var/www/images and then use the url
# localhost/images/ 
