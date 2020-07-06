from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')


    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.user.email

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    product_number = models.PositiveIntegerField()
    img = models.FileField(upload_to='products\%Y%m%d')