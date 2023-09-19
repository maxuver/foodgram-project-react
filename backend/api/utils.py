from datetime import datetime
from django.db.models import Sum
from recipes.models import RecipeIngredients


def create_shopping_cart(user, request):

    ingredients = RecipeIngredients.objects.filter(
        recipe__shopping_cart__user=request.user
    ).values(
        'ingredient__name',
        'ingredient__measurement_unit'
    ).annotate(cart_amount=Sum('amount'))

    today = datetime.today()
    shopping_list = (
        f'Список покупок пользователя: {user.get_full_name()}\n\n'
        f'Дата: {today:%Y-%m-%d}\n\n'
    )
    shopping_list += '\n'.join([
        f'- {ingredient['ingredient__name']} '
        f'({ingredient['ingredient__measurement_unit']})'
        f' - {ingredient['cart_amount']}'
        for ingredient in ingredients
    ])
    shopping_list += f'\n\nFoodgram - {today:%Y}'

    return shopping_list
