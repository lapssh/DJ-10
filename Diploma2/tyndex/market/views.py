from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


# def index_view(request):
#     print('=' * 80)
#     #products = Product.objects.all()
#     # template = 'market/test.html'
#     template = loader.get_template('index.html')
#     context = {
#
#     }
#     return HttpResponse(template.render(context, request))
def index_view(request):
    print('test')
    print('=' * 80)
    #products = Product.objects.all()
    # template = 'market/test.html'
    #template = loader.get_template('index.html')
    context = {

    }
    return render(request, 'index.html', context)