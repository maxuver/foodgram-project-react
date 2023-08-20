import csv

from django.conf import settings
from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка из csv файла'

    def handle(self, *args, **kwargs):
        data_path = settings.BASE_DIR
        with open(
            f'{data_path}/data/ingredients.csv', 'r', encoding='utf-8'
        ) as file:
            amount_old = Ingredient.objects.all().count()
            reader = csv.DictReader(
                file, fieldnames=['name', 'measurement_unit'])
            Ingredient.objects.bulk_create(
                [Ingredient(**data) for data in reader], ignore_conflicts=True)
        amount = Ingredient.objects.all().count()
        self.stdout.write(self.style.SUCCESS(
            f'Загружено ингредиентов: {amount - amount_old} шт. \n'
            f'Ингредиентов в базе: {amount} шт.'
        ))
