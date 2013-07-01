'''
Created on 01/07/2013

@author: Seb
'''

from django.contrib import admin
from onlineOrderingApp.models import *   


class OnlineOrderInline(admin.StackedInline):
    model = OrderItem
    can_delete = False
    verbose_name_plural = 'Order Details'

class OnlineOrderAdmin(admin.ModelAdmin):
    inlines = (OnlineOrderInline, )

admin.site.register(OnlineOrder, OnlineOrderAdmin)


