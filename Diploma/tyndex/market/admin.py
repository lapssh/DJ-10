from django.contrib import admin
# Register your models here.

from .models import Article
from .models import Section
from .models import Category
from .models import Product
from .models import Customer
from .models import Order
from .models import ProductsInOrder

admin.site.register(Article)
admin.site.register(Section)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ProductsInOrder)