"""tyndex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

from market.views import index, view_all_articles, one_article, product_view, product_list_view, show_cart_view, \
    add_to_cart

#     path('accounts/login/', LoginView.as_view(), name='login'),
urlpatterns = [
    path('index.html', index, name='index'),
    path('', index),
    path('market/', include('market.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('articles/read/<str:name>', one_article, name='one_article'),
    path('articles/', view_all_articles, name='view_all_articles'),
]
urlpatterns += [
    path('product_list_view', product_list_view, name='product_list_view'),
    path('<str:section_slug>/<str:category_slug>/<str:slug>', product_view, name='product'),
    path('<str:section_slug>/<str:category_slug>', product_list_view, name='products'),
    path('', product_list_view, name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('cart/', show_cart_view, name='show_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
]