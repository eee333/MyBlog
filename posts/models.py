from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    foto = models.ImageField(upload_to='posts/', blank=True, verbose_name='Фото')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.title} ({self.author})'

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
