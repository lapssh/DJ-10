from django.shortcuts import render


def home_view(request):
    template_name = 'app/home.html'
    return render(request, template_name)


def about_view(request):
    template_name = 'app/about2.html'
    context = {
        "about": 'active'
    }
    return render(request, template_name, context)


def contacts_view(request):
    template_name = 'app/contacts2.html'
    context = {
        "contacts": 'active'
    }
    return render(request, template_name, context)


def examples_view(request):
    template_name = 'app/examples2.html'

    items = [{
        'title': 'Apple II',
        'text': 'Легенда',
        'img': '/static/ii.jpg'
    }, {
        'title': 'Macintosh',
        'text': 'Свежие новинки октября 1983-го',
        'img': '/static/mac.jpg'
    }, {
        'title': 'iMac',
        'text': 'Оригинальный и прозрачный',
        'img': '/static/imac.jpg'
    }]
    context = {
        'items': items,
        "examples": 'active'
    }
    return render(request, template_name,
                  context)


def mayka_view(request):
    template_name = 'app/about2.html'
    return render(request, template_name)
