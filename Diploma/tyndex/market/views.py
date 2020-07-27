from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Product, Article, Category

# Create your views here.
PRODUCTS_PER_PAGE = 3

def index(request):
    print('=' * 80)
    articles = Article.objects.order_by('-published')

    context = {
        'articles': articles,
    }

    return render(request, 'articles.html', context)
    # products = Product.objects.all()
    # # template = 'market/test.html'
    # template = loader.get_template('index.html')
    # context = {
    #     'products': products
    # }
    # return HttpResponse(template.render(context, request))
    # render(request, template, context)
    # render(request, template, context)

    # return HttpResponse("Здесь будет интернет-магазин")


def view_all_articles(request):
    articles = Article.objects.order_by('-created')

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def one_article(request, name=None):
    articles = Article.objects.filter(name=name)
    context = {'articles': articles}

    article = Article.objects.filter(name=name).first()

    if not article:
        raise Http404('Error 404! Sorry')

    return render(request, 'articles.html', context)

def cart(request):
    template = loader.get_template('market/cart.html')
    context = {}
    return HttpResponse(template.render(context, request))

def smartphones(request):
    template = loader.get_template('market/smartphones.html')
    context = {}
    return HttpResponse(template.render(context, request))

def accessories(request):
    template = loader.get_template('market/accessories.html')
    context = {}
    return HttpResponse(template.render(context, request))

def product_list_view(request, section_slug=None, category_slug=None):
    products = Product.objects.all()
    category_name = 'Все товары:'

    if section_slug and category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = list(category.products.all())
        category_name = category.name.capitalize()

    page = request.GET.get('page')
    paginator = Paginator(products, PRODUCTS_PER_PAGE)
    products_paginate = paginator.get_page(page)

    context = {
        'category_name': category_name,
        'products_paginate': products_paginate,
    }

    return render(request, 'product-list.html', context)


def product_view(request, section_slug, category_slug, slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(category.products, slug=slug)

    context = {'product': product, }

    return render(request, 'product.html', context)

def show_cart_view(request):
    next_page = request.GET.get('next')
    context = {
        'next': next_page,
    }
    cart = request.session.get('cart', None)
    if cart:
        products = {}
        product_list = Product.objects.filter(
            pk__in=cart.keys()).values(
            'id', 'name', 'img', 'price', )
        for product in product_list:
            products[str(product['id'])] = product
        for key in cart.keys():
            cart[key]['product'] = products[key]
        context['cart'] = cart
    return render(request, 'cart.html', context)


def add_to_cart(request):
    next_page = request.GET.get('next')
    if request.method == 'POST':
        product_pk = request.GET.get('product_id')
        if 'cart' not in request.session:
            request.session['cart'] = {}
        cart = request.session.get('cart')
        if product_pk in cart:
            cart[product_pk]['quantity'] += 1
        else:
            cart[product_pk] = {
                'quantity': 1,
            }
    #print(request.get('product_id'))
    request.session.modified = True
    return redirect(next_page)
    # return render(request, 'cart.html', context)