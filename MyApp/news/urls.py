from django.urls import path
from . import views  # Импортируем ваши представления

urlpatterns = [
    path('', views.home_news, name='home_news'),  # Главная страница
path('create_news/', views.create_news, name='add_news'),
]