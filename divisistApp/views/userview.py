#DJANGO RESTFRAMWORK
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
#DJANGO
from django.contrib.auth import authenticate
#LOCAL
from divisistApp.serializer import UserSerializer
from divisistApp.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        return Response({'message': 'Hello World'})