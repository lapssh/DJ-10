from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    product_number = models.PositiveIntegerField()
    img = models.FileField(upload_to='products\%Y%m%d')