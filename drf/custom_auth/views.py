from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post', 'put', 'patch']
