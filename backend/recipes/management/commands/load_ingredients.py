import csv

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.import_ingredients()
        print('Загрузка ингредиентов успешно выполнена.')

    def import_ingredients(self, file='ingredients.csv'):
        print(f'Данные загружаются из {file}')
        path = f'./data/{file}'
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                Ingredient.objects.update_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )