from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from .models import Product, Article, Category, Order, ProductsInOrder, Customer

PRODUCTS_PER_PAGE = 6


def index(request):
    try:
        print('=' * 80)
        articles = Article.objects.order_by('-published')

        context = {
            'articles': articles,

        }
        print(context)

        return render(request, 'articles.html', context)
    except:
        raise Http404("Page does not exist")


def view_all_articles(request):
    articles = Article.objects.order_by('-created')

    context = {
        'articles': articles,
    }
    print(context)

    return render(request, 'index.html', context)


def one_article(request, name=None):
    articles = Article.objects.filter(name=name)
    context = {'articles': articles}
    print(context)

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
    try:

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
    except:
        raise Http404("Page does not exist")


def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)


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
            print(products, '\n')
        for key in cart.keys():
            cart[key]['product'] = products[key]
            print(cart[key]['product'], '\n')
        context['cart'] = cart
        context['products_count'] = len(cart)
        print(80 * '=')
        print(len(cart))
        # pprint(context['cart'])
        pprint(request.session['cart'])
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
    # print(request.get('product_id'))
    request.session.modified = True
    return redirect(next_page)
    # return render(request, 'cart.html', context)


def order_view(request):
    if request.method == 'POST':
        # customer_pk = request.user.customer.pk
        # print(request.META)
        cart = request.session['cart']
        print('items: ', request.session.__dict__)
        customer_id_ = request.session['_auth_user_id']
        print('ID пользователя: ', request.session['_auth_user_id'])
        customer_pk = request.session['_auth_user_id']
        print(cart)
        customer_ = Customer.objects.get(user_id=customer_id_)
        print(customer_)

        cart = request.session['cart']

        if len(cart) > 0:
            order = Order.objects.create(customer=customer_)

            for key, value in cart.items():
                product = Product.objects.get(pk=key)
                quantity = value['quantity']
                ProductsInOrder.objects.create(order=order,
                                               product=product,
                                               quantity=quantity,
                                               )
            request.session['cart'] = {}
            request.session.modified = True

            messages.success(request,
                             f"Спасибо, {customer_}! Ваш заказ оформлен."
                             f"\nОжидайте доставку, наш курьер скоро с вами свяжется.")

    return redirect('show_cart')
