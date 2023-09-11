from colorfield.fields import ColorField
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        'Название',
        max_length=200
    )

    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=200
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        unique_together = ('name', 'measurement_unit',)
        ordering = ('name',)

    def str(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    name = models.CharField(
        'Название тега',
        max_length=200,
        unique=True
    )

    color = ColorField(
        'Цвет в формате HEX',
        format='hex',
        default='#778899',
        unique=True,
    )

    slug = models.SlugField(
        'Уникальный слаг',
        max_length=200,
        unique=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def str(self):
        return self.name
