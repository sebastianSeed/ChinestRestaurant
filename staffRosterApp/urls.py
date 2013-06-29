from django.conf.urls import patterns, url

from staffRosterApp import views

urlpatterns = patterns('',
    url(r'^view', views.roster ,name='roster'),
    url(r'^updateRoster', views.updateRoster,name='updateRoster'),
    url(r'^jsonfeed', views.rosterJsonFeed,name='jsonFeed'),
    

    
    
    
)