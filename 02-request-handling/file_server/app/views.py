import datetime
from django.http import HttpResponse

from django.shortcuts import render
from django.conf import settings

BASE_DIR = settings.BASE_DIR


def file_list(request):
    template_name = 'index.html'
    files_path = BASE_DIR+'\\files'

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': [
            {'name': 'server.01',
             'ctime': datetime.datetime(2018, 1, 1),
             'mtime': datetime.datetime(2018, 1, 2)},
            {'name': 'server.02',
             'ctime': datetime.datetime(2018, 1, 1),
             'mtime': datetime.datetime(2018, 1, 2)},
            {'name': 'server.03',
             'ctime': datetime.datetime(2018, 1, 1),
             'mtime': datetime.datetime(2018, 1, 2)}
        ]
        # 'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    }
    print(context)
    #return HttpResponse('qj')
    print('Отработала file_list')
    print(f'{files_path}=')
    return render(request, template_name, context)


# def file_content(request):
def file_content(request, name='server.01'):
    print('Начала file_content'
          '')
# def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': 'server.01', 'file_content': 'File content!'}
    )

