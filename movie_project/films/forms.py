from .models import News_post
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['movie_title', 'film_content', 'review', 'pub_date']
        widgets = {
                'movie_title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
                'film_content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое содержание'}),
                'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
                'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
                }