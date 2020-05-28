from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    response = request.GET.get('from-landing')
    if response == 'original':
        counter_show['original'] += 1
        print(f'{counter_show["original"]=}  {response}')
    elif response == 'test':
        counter_show['test'] += 1
        print(f'{counter_show["test"]=}  {response}')
    else:
        counter_show['other'] += 1
        print(f'{counter_show["other"]=}  {response}')
    return render_to_response('index.html')


def landing(request):
    response = request.GET.get('ab-test-arg')
    if response == 'original':
        counter_click['original'] += 1
        print(f'{counter_click["original"]=}')
        return render_to_response('landing.html')
    elif response == 'test':
        counter_click['test'] += 1
        print(f'{counter_click["test"]=}')
        return render_to_response('landing_alternate.html')
    else:
        counter_click['other'] += 1
        print(f'{counter_click["other"]=}')
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render_to_response('landing.html')


def stats(request):
    if counter_click['original'] == 0:
        original_conversion = 1
    else:
        original_conversion = round(counter_show['original'] / counter_click['original'], 2)
    if counter_click['test'] == 0:
        test_conversion = 1
    else:
        test_conversion = round(counter_show['test'] / counter_click['test'], 2)

    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
