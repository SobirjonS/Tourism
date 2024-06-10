from django.shortcuts import render
from . import models


def main(request):
    data_news = models.New.objects.all().order_by('-id')[:6]
    data_lendmarks = models.Lendmark.objects.all().order_by('-id')[:6]
    data_statistics = models.Statistic.objects.all().order_by('-id')[:5]
    data_hotels = models.Hotel.objects.all().order_by('-id')[:6]
    data_foods = models.Food.objects.all().order_by('-id')[:6]
    context = {'data_news': data_news, 
               'data_lendmarks': data_lendmarks, 
               'data_statistics':data_statistics,
               'data_foods':data_foods,
               'data_hotels':data_hotels,
               }
    return render(request, 'main/index.html', context)


def committee(request):
    return render(request, 'main/pages/committee.html')

    
def legislation(request):
    return render(request, 'main/pages/legislation.html')


def press_service(request):
    return render(request, 'main/pages/press_service.html')


def services(request):
    return render(request, 'main/pages/services.html')


def research(request):
    return render(request, 'main/pages/research.html')


def privilege(request):
    return render(request, 'main/pages/privilege.html')