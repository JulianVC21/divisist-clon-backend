#DJANGO RESTFRAMWORK
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
#DJANGO
from django.contrib.auth import authenticate
#LOCAL
from divisistApp.serializer import UserSerializer, UserRecoverySerializer, UserUpdatePasswordSerializer
from divisistApp.models import User
import uuid

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        return Response({'message': 'Hello World'})
    
    @action(detail=False, methods=['post'])
    def recovery_password(self, request):

        serializer = UserRecoverySerializer(data = request.data)

        if serializer.is_valid():
            email = serializer.validated_data['institutional_email']

            try:
                user = User.objects.get(institutional_email = email)
            except User.DoesNotExist:
                return Response({'message': 'Datos invalidos'}, status=status.HTTP_404_NOT_FOUND)
            
            user.recovery_token = uuid.uuid4();
        
            user.save()

            return Response({
                    'recovery_token': user.recovery_token,
                    'message': 'Se ha generado un token de restauración de contraseña'
                })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['post'])
    def update_password(self, request):

        serializer = UserUpdatePasswordSerializer(data = request.data)

        if serializer.is_valid():
            recovery_token = serializer.validated_data['recovery_token']
            new_password = serializer.validated_data['new_password']

            try:
                user = User.objects.get(recovery_token=recovery_token)
            except User.DoesNotExist:
                return Response({'message': 'Token Invalido'}, status=status.HTTP_404_NOT_FOUND)
            
            user.password = new_password
            user.save()

            return Response( {'message': 'Contraseña actualizada'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)