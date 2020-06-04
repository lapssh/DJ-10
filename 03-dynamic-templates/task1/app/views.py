from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', 'r', encoding='utf-8') as f:
        data = csv.reader(f, delimiter=';')
        header = next(data)
        result = []
        years = [str(x) for x in range(1991,2019)]
        sum_counter = 0 # каунтер для обнаружения последнего столбца
        for row in data:
            data_ = []
            for td in row:
                td_dict = {}
                sum_counter += 1
                if sum_counter == 14:
                    td_dict['data'] = td
                    td_dict['bgcolor'] = 'gray'
                    sum_counter = 0
                    data_.append(td_dict)
                    continue
                if td in years: # проверяем, что столбец - не год.
                    td_dict['data'] = td
                    td_dict['bgcolor'] = 'white'
                    data_.append(td_dict)
                    continue
                if not td:
                    td_dict['data'] = '-'
                    td_dict['bgcolor'] = 'white'
                    data_.append(td_dict)
                    continue
                elif float(td) >= 5:
                    td_dict['data'] = td
                    td_dict['bgcolor'] = 'darkred'
                elif float(td) >= 2:
                    td_dict['data'] = td
                    td_dict['bgcolor'] = 'crimson'
                elif float(td) >= 1:
                    td_dict['data'] = td
                    td_dict['bgcolor'] = 'lightCoral'
                elif float(td) >= 0:
                    td_dict['data'] = td
                    td_dict['bgcolor'] = 'white'
                elif float(td) < 0:
                    td_dict['data'] = td
                    td_dict['bgcolor'] = 'green'

                data_.append(td_dict)
                continue
            result.append(data_)


    context = {
        'header': header,
        'rows': result
    }
    return render(request, template_name, context)
