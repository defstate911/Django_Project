from django.db import models


class News_post(models.Model):
    movie_title = models.CharField('Название фильма', max_length=100)
    film_content = models.TextField('Краткое содержание')
    review = models.TextField('Отзыв')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.movie_title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
