from django.urls import path
from . import views  # Импортируем ваши представления

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('flower_ciklamen/', views.flower_ciklamen, name='flower_ciklamen'),  # Цикламен
    path('flower_kaktus/', views.flower_kaktus, name='flower_kaktus'),  # Кактус
    path('flower_tolstyanka/', views.flower_tolstyanka, name='flower_tolstyanka'),  # Толстянка
]
