from django.conf.urls import patterns, url

from staffRosterApp import views

urlpatterns = patterns('',
    url(r'^view/$', views.roster ,name='roster'),
         url(r'^viewAvailabity/$', views.availabilityRoster ,name='availabilityRoster'),

    url(r'^createShift/$', views.createShift,name='createShift'),
    url(r'^jsonfeed/$', views.rosterJsonFeed,name='jsonFeed'),
    url(r'^availabilityJsonFeed/$', views.availabilityJsonFeed,name='jsonFeed'),

    url(r'^deleteShift/$', views.deleteShift,name='deleteShift'),
    url(r'^editShift/$', views.editShift ,name='editShift'),


    
    
    
)