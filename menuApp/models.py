from django.db import models

# Create your models here.

#Split into another table to allow categories to be added/deleted etc
class menuCategory(models.Model):   
    name  = models.CharField(max_length=25)

#Used to generate menu view for customers
class menuItem(models.Model):
    name        = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    image       = models.ImageField(upload_to='foodPhotos')
    category    = models.ForeignKey(menuCategory)

   
#Used to track online orders
class OnlineOrder (models.Model):    
    confirmed   = models.BooleanField()
    orderTime   = models.DateTimeField(auto_now_add=True)
    totalCost   = models.DecimalField(decimal_places =2 , max_digits=8)
    orderItems  = models.ForeignKey(menuItem)

    
