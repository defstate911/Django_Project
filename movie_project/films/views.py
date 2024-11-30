from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

def index(request):
    films = News_post.objects.all()
    return render(request,'films/index.html', {'films': films})

def add_film(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Данные были заполнены некорректно"
    form = News_postForm()
    return render(request, 'films/add_film.html', {'form': form, 'error': error})

