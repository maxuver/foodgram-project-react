from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models import UniqueConstraint


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user', 'пользователь'
        ADMIN = 'admin', 'администратор'

    role = models.CharField(
        'роль',
        max_length=10,
        default=Role.USER,
        choices=Role.choices
    )
    password = models.CharField(
        'пароль',
        max_length=150
    )

    email = models.EmailField(
        'адрес электронной почты',
        max_length=254,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def str(self):
        return self.username
