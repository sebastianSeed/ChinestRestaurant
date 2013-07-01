from django.db import models

# Create your models here.
class menuItem(models.Model):
    name        = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    image       = models.ImageField(upload_to='foodPhotos')

