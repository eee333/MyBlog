from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.BigIntegerField(null=True, blank=True, verbose_name='Телефон')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
