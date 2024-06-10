from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main import models


#main
@login_required
def main(request):
    return render(request, 'dash/main/index.html')


#news CRUD
@login_required
def news(request):
    data = models.New.objects.all()
    return render(request, 'dash/main/news/news.html', {'data':data})


@login_required
def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('file')
        models.New.objects.create(title=title, body=body, image=image)
        return redirect('dash:news')
    return render(request, 'dash/main/news/create.html')


@login_required
def update_news(request, pk):
    news = models.New.objects.get(pk = pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('file')
        news.title = title
        news.body = body
        news.image = image
        news.save()
        return redirect('dash:news')
    return render(request, 'dash/main/news/update.html', {'data':news})


@login_required
def delete_news(request, pk):
    news = models.New.objects.get(pk = pk)
    news.delete()
    return redirect('dash:news')


#lendmarks CRUD
@login_required
def lendmarks(request):
    data = models.Lendmark.objects.all()
    return render(request, 'dash/main/lendmarks/lendmarks.html', {'data':data})


@login_required
def create_lendmark(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('file')
        models.Lendmark.objects.create(title=title, body=body, image=image)
        return redirect('dash:lendmarks')
    return render(request, 'dash/main/lendmarks/create.html')


@login_required
def update_lendmark(request, pk):
    news = models.Lendmark.objects.get(pk = pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('file')
        news.title = title
        news.body = body
        news.image = image
        news.save()
        return redirect('dash:lendmarks')
    return render(request, 'dash/main/lendmarks/update.html', {'data':news})


@login_required
def delete_lendmark(request, pk):
    news = models.Lendmark.objects.get(pk = pk)
    news.delete()
    return redirect('dash:lendmarks')


#hotels CRUD
@login_required
def hotels(request):
    data = models.Hotel.objects.all()
    return render(request, 'dash/main/hotels/hotels.html', {'data':data})


@login_required
def create_hotel(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('file')
        models.Hotel.objects.create(title=title, body=body, image=image)
        return redirect('dash:hotels')
    return render(request, 'dash/main/hotels/create.html')


@login_required
def update_hotel(request, pk):
    news = models.Hotel.objects.get(pk = pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('file')
        news.title = title
        news.body = body
        news.image = image
        news.save()
        return redirect('dash:hotels')
    return render(request, 'dash/main/hotels/update.html', {'data':news})


@login_required
def delete_hotel(request, pk):
    news = models.Hotel.objects.get(pk = pk)
    news.delete()
    return redirect('dash:hotels')

#foods CRUD
@login_required
def foods(request):
    data = models.Food.objects.all()
    return render(request, 'dash/main/foods/foods.html', {'data':data})


@login_required
def create_food(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('file')
        models.Food.objects.create(title=title, body=body, image=image)
        return redirect('dash:foods')
    return render(request, 'dash/main/foods/create.html')


@login_required
def update_food(request, pk):
    news = models.Food.objects.get(pk = pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('file')
        news.title = title
        news.body = body
        news.image = image
        news.save()
        return redirect('dash:foods')
    return render(request, 'dash/main/foods/update.html', {'data':news})


@login_required
def delete_food(request, pk):
    news = models.Food.objects.get(pk = pk)
    news.delete()
    return redirect('dash:foods')

#statistics CRUD
@login_required
def statistics(request):
    data = models.Statistic.objects.all()
    return render(request, 'dash/main/statistics/statistics.html', {'data':data})


@login_required
def create_statistic(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        number = request.POST.get('number')
        icon = request.FILES.get('file')
        print(title)
        print(number)
        print(icon)
        models.Statistic.objects.create(title=title, number=number, icon=icon)
        return redirect('dash:statistics')
    return render(request, 'dash/main/statistics/create.html')


@login_required
def update_statistic(request, pk):
    news = models.Statistic.objects.get(pk = pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        number = request.POST.get('number')
        icon = request.FILES.get('file')
        news.title = title
        news.number = number
        news.icon = icon
        news.save()
        return redirect('dash:statistics')
    return render(request, 'dash/main/statistics/update.html', {'data':news})


@login_required
def delete_statistic(request, pk):
    news = models.Statistic.objects.get(pk = pk)
    news.delete()
    return redirect('dash:statistics')
