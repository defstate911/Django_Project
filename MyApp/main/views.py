from django.http import HttpResponse #использовалось  при создании примеров
from django.shortcuts import render


# упрощенные страницы для обучения
# def home(request):
#     return HttpResponse('<h1>Это открывается домашняя страница home</h1>')

# def data(request):
#     return HttpResponse('<h1>Это открывается страница data</h1>')
#
# def test(request):
#     return HttpResponse('<h1>Это открывается страница test</h1>')

def home(request):
    return render(request, 'main/home.html')

def flower_ciklamen(request):
    return render(request, 'main/flower_ciklamen.html')

def flower_tolstyanka(request):
    return render(request, 'main/flower_tolstyanka.html')

def flower_kaktus(request):
    return render(request, 'main/flower_kaktus.html')
