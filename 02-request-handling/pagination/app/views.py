from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    bus_st = []
    with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as csvfile:
        reader  = csv.DictReader(csvfile)
        for row in reader:
            bus_st.append(row)

    paginator = Paginator(bus_st, 10)
    page = request.GET.get('page', 1)
    page_object = paginator.get_page(page)

    current_page = page
    next_page_url = '?page='+str(int(page)+1)
    if int(current_page) > 1:
        prev_page_url = '?page=' + str(int(page) - 1)
    else:
        prev_page_url = None
    return render_to_response('index.html', context={
        'bus_stations': page_object,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
    # return render_to_response('index.html', context={
    #     'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
    #     'current_page': current_page,
    #     'prev_page_url': None,
    #     'next_page_url': next_page_url,
    # })

