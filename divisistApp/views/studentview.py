#DJANGO RESTFRAMWORK
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
#DJANGO
from django.contrib.auth import authenticate
#LOCAL
from divisistApp.serializer import StudentLoginSerializer, StudentSerializer
from divisistApp.models import Student
from ..utils import verify_jwt_token

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

            # Buscamos al estudiante por su dni y codigo (carrera + consecutivo) para saber que estos datos corresponden al estudiante
            try:
                student = Student.objects.get(dni=dni, career=career, consecutive=consecutive)
            except Student.DoesNotExist:
                return Response({'message': 'Datos invalidos'}, status=status.HTTP_404_NOT_FOUND)
            
            # Verificacion de la contraseña
            if student.check_password(password): 
                # Si la contraseña es válida, generamos el JWT
                refresh = RefreshToken.for_user(student)
                access_token = str(refresh.access_token)

                return Response({
                    'message': 'Login successful',
                    'access_token': access_token,
                }, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Código o Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def auth_login(self, request):
        token = request.headers.get('Authorization', )
        # Verificamos si el token existe
        if token is None:
            return Response({'message': 'Token invalido'}, status=400)
        
        return Response({'message': token})

        # Eliminar  'Bearer ' del token
        token = token.split(' ')[1] if token.startswith('Bearer ') else token

        try:
            # Verificar token
            user_id = verify_jwt_token(token)
            return Response({'message': 'Token valido', 'user_id': user_id})

        except AuthenticationFailed as e:
            return Response({'message': f'Fallo en la autenticación: {str(e)}'}, status=401)

        except Exception as e:
            return Response({'message': f'Error: {str(e)}'}, status=500)
        
    @action(detail=False, methods=['get'])
    def auth_test(self, request):
        token = 'hello world'
        return Response({'message': token})