from rest_framework import viewsets
from divisistApp.serializer import UserSerializer
from divisistApp.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer