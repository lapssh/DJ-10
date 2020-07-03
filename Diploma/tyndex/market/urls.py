from django.urls import path

from .views import index
from .views import cart
from .views import smartphones
from .views import accessories

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('cart.html', cart, name='cart'),
    path('smartphones.html', smartphones, name='smartphones'),
    path('accessories.html', accessories, name='accessories'),
]