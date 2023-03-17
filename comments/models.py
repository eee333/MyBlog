from django.db import models

from posts.models import Post
from users.models import User


class Comment(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.author}, {self.post}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
