from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime
from django.utils import timezone

def verify_jwt_token(token):
    # Función para verificar la validez de un JWT.
    # Si el token es válido, devuelve el usuario autenticado.
    # Si no es válido, lanza una excepción.
    try:
        # Decodificar el JWT
        decoded_token = AccessToken(token)

        # Verificar si el token ha expirado
        if decoded_token['exp'] < datetime.now(timezone.utc).timestamp():
            raise AuthenticationFailed('Sesión expirada')

        # Si el token es válido, se puede acceder a los datos del usuario
        user_id = decoded_token['user_id']
        
        # Aquí podrías devolver el usuario directamente, si es necesario:
        # user = User.objects.get(id=user_id)
        
        return user_id  # O devolver el usuario si lo necesitas (user)

    except Exception as e:
        raise AuthenticationFailed(f'Sesión invalida o expirada: {str(e)}')
