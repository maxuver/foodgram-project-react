from users.models import User, Subscribe
from djoser.views import UserViewSet
from .serializers import CustomUserSerializer, IngredientSerializer, TagSerializer, SubscribeSerializer
from recipes.models import Ingredient, Tag, Recipe
from rest_framework.viewsets import ReadOnlyModelViewSet
from .paginations import ProjectPagination
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    @action(
        detail=True,
        methods=('post', 'delete'),
        permission_classes=(IsAuthenticated,)
    )
    def subscribe(self, request, **kwargs):
        user = request.user
        author_id = self.kwargs.get('id')
        author = get_object_or_404(User, id=author_id)

        if request.method == 'POST':
            serializer = SubscribeSerializer(
                author,
                data=request.data,
                context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            Subscribe.objects.create(user=user, author=author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        subscription = get_object_or_404(
            Subscribe,
            user=user,
            author=author
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        permission_classes=(IsAuthenticated,)
    )
    def subscriptions(self, request):
        user = request.user
        queryset = User.objects.filter(subscribing__user=user)
        pages = self.paginate_queryset(queryset)
        serializer = SubscribeSerializer(
            pages,
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
