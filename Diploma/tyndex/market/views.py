from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product
# Create your views here.

def index(request):
    print('=' * 80)
    products = Product.objects.all()
    # template = 'market/test.html'
    template = loader.get_template('market/index.html')
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))
    # render(request, template, context)
    # render(request, template, context)

    # return HttpResponse("Здесь будет интернет-магазин")