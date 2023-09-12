from users.models import User
from djoser.serializers import UserSerializer
from recipes.models import Ingredient, Tag
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
        )


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
