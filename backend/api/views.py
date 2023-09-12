from users.models import User
from djoser.views import UserViewSet
from .serializers import CustomUserSerializer, IngredientSerializer, TagSerializer
from recipes.models import Ingredient, Tag
from rest_framework.viewsets import ReadOnlyModelViewSet
from .paginations import ProjectPagination


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None

