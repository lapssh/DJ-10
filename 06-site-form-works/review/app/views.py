from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product=product).order_by('-id')

    if 'reviewed_products' not in request.session.keys():
        request.session['reviewed_products'] = []

    if request.method == 'GET':
        form = ReviewForm

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        text_ = ReviewForm(request.POST)['text'].value()
        Review.objects.create(text=text_, product=product)
        request.session['reviewed_products'].append(product.id)
        request.session.modified = True

    context = {
        'form': form,
        'product': product,
        'reviews': reviews
    }

    if product.id in request.session['reviewed_products']:
        context['is_review_exist'] = True

    return render(request, template, context)
