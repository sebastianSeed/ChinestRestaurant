from django.conf.urls import patterns, url

from menuApp import views

urlpatterns = patterns('',
url(r'^view/$', views.customerMenuView),
url(r'^placeOrder/$', views.placeOrder),
url(r'^admin/$', views.staffOrderAdmin),



    
    
    
)