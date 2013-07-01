from django.db import models

class OnlineOrder (models.Model):    
    confirmed = models.BooleanField()
    orderTime = models.DateTimeField(auto_now_add=True)
    totalCost = models.DecimalField(decimal_places =2 , max_digits=8)
    
class OrderItem (models.Model):
    item  = models.ForeignKey('menuApp.menuItem')
    order = models.ForeignKey(OnlineOrder)
    price = models.DecimalField(decimal_places =2 , max_digits=8)
    

    
    
    