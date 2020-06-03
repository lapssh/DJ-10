from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', 'r', encoding='utf-8') as f:
        data = csv.reader(f, delimiter=';')
        header = next(data)
        print(f'{header=}')
        data_ = []
        result = []

        for row in data:  # создаю данные для таблицы
            for td in row:
                td_dict = {}  # передам на клиент значения словарём со значением и цветом
                if not td:  # если значения в клетке нет - передадим прочерк
                    td_dict['data'] = '-'
                    td_dict['bgcolor'] = 'white'
                    data_.append(td_dict)
                    continue
                elif float(td) >= 5:
                    td_dict['data'] = td
                    td_dict['bgcolor'] = 'dark_red'
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

                data_.append(td_dict)  # добавляем данные ячейки
                print(td_dict)
                print()
            result.append(data_)


    context = {
        'header': header,
        'rows': result
    }
    return render(request, template_name, context)
    # template_name = 'inflation.html'
    #
    # # чтение csv-файла и заполнение контекста
    # data_ = []
    #
    # with open('inflation_russia.csv', 'r', encoding='utf-8') as f:
    #     data = csv.reader(f, delimiter = ';')
    #     for i in data:
    #         data_.append(i)
    #         print(i)
    # data2 = data_.pop(0)
    #
    # # for i in data:
    # #     data_.append(i)
    # #     print(i)
    # print('точка останова')
    # context = {
    #     'header': data2,
    #     'rows': data_}
    # # context = data
    # return render(request, template_name,
    #               context)