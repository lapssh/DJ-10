from django.shortcuts import render
from .models import Phone
from operator import attrgetter


def show_catalog(request):
    template = 'catalog.html'
    my_phones = Phone.objects.all()
    response = request.GET.get('sort')
    if response == 'name':
        print('Сортировка по имени')
        my_phones = sorted(my_phones, key=attrgetter('name'))
    elif response == 'min_price':
        print('Сортировка по убыванию')
        my_phones = sorted(my_phones, key=attrgetter('price'))
    elif response == 'max_price':
        print('Сортировка по возрастанию')
        my_phones = sorted(my_phones, key=attrgetter('price'), reverse=True)
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
