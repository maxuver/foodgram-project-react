from users.models import User
from djoser.views import UserViewSet
from .serializers import CustomUserSerializer

class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
