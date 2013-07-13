'''
Created on 21/06/2013

@author: Seb
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from staffRosterApp.models import *    
from menuApp.models import menuItem



# Add the employee details to the create user form in
#the framework provided admin page eg mywebsite/admin. 
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Staff Details'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )
    #Override the field set options     
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1','password2')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
