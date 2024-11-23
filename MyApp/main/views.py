from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Это открывается домашняя страница home</h1>')

def data(request):
    return HttpResponse('<h1>Это открывается страница data</h1>')

def test(request):
    return HttpResponse('<h1>Это открывается страница test</h1>')
