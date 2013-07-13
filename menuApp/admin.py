'''
Created on 01/07/2013

@author: Seb
'''
from django.contrib import admin
from menuApp.models import *   



#Display category widget when editing menu items
#Allows users to add categories from menu item page
    
admin.site.register(menuCategory) 
admin.site.register(menuItem)