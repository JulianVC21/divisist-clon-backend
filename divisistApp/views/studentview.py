#DJANGO RESTFRAMWORK
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

#LOCAL
from divisistApp.serializer import StudentLoginSerializer, StudentSerializer
from divisistApp.models import Student
from ..utils.verify_jwt import encode_jwt, decode_jwt

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):

        serializer = StudentLoginSerializer(data=request.data)

        if serializer.is_valid():
            dni = serializer.validated_data['dni']
            career = serializer.validated_data['career']
            consecutive = serializer.validated_data['consecutive']
            password = serializer.validated_data['password']
            dni = serializer.validated_data['dni']

            # Buscamos al estudiante por su dni y codigo (carrera + consecutivo) para saber que estos datos corresponden al estudiante
            try:
                student = Student.objects.get(career=career, consecutive=consecutive, dni=dni)
            except Student.DoesNotExist:
                return Response({'message': 'Datos invalidos'}, status=status.HTTP_404_NOT_FOUND)
            
            # Verificacion de la contraseña
            if student.check_password(password):
                # Si la contraseña es válida, generamos el JWT
                token = encode_jwt(student.pk);

                return Response({
                    'message': 'Login successful',
                    'access_token': token,
                }, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Datos invalidos'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def auth_login(self, request):
        token = request.headers.get('Authorization')
        
        # Verificamos si el token existe
        if token is None:
            return Response({'message': 'Token invalido'}, status=400)

        # Eliminar  'Bearer ' del token
        token = token.split(' ')[1] if token.startswith('Bearer ') else token

        try:
            # Verificar token
            decoded = decode_jwt(token)

            return Response({'auth_login':decoded})

        except AuthenticationFailed as e:
            return Response({'message': f'Fallo en la autenticación: {str(e)}'}, status=401)

        except Exception as e:
            return Response({'message': f'Error: {str(e)}'}, status=500)
        