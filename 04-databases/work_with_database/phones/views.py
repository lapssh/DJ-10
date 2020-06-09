from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    response = request.GET.get('sort')
    if response == 'name':
        print('Сортировка по имени')
    elif response == 'min_price':
        print('Сортировка по цене')
    template = 'catalog.html'
    my_phones = Phone.objects.all()
    context = {'my_phones': my_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(slug)
    my_phones = Phone.objects.all()
    phones_by_slug = []
    for p in my_phones:
        if p.slug == slug:
            print('B I N G O')
            phones_by_slug.append(p)
    context = {'phones_by_slug': phones_by_slug}
    return render(request, template, context)
