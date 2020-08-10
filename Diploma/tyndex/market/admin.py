from django.contrib import admin
# Register your models here.
from .models import Article
from .models import Section
from .models import Category
from .models import Product
from .models import Customer, User
from .models import Order
from .models import ProductsInOrder


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder

    verbose_name = 'Заказанный товар'
    verbose_name_plural = 'Заказанные товары'


class OrderAdmin(admin.ModelAdmin):
    ordering = ('created', 'id')
    list_display = ('customer', 'quantity', 'created',)
    inlines = (ProductsInOrderInline,)

    def quantity(self, obj):
        return ProductsInOrder.objects.filter(order=obj).count()

    quantity.short_description = 'Количество единиц'


admin.site.register(Article)
admin.site.register(Section)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
