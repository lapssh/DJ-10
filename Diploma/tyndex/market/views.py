from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    print('=' * 80)
    template = 'market/test.html'
    context = {
        'test': 'test',
    }
    render(request, template, context)
    # render(request, template, context)

    # return HttpResponse("Здесь будет интернет-магазин")