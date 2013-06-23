from django.conf.urls import patterns, url

from staffRosterApp import views

urlpatterns = patterns('',
    url(r'^view', views.rosterView ,name='roster'),

    
    
    
)