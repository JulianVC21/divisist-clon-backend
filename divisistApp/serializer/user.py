from rest_framework import serializers
from divisistApp.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserRecoverySerializer(serializers.Serializer):
    institutional_email = serializers.EmailField( required = True)

class UserCheckTokenSerializer(serializers.Serializer):
    recovery_token = serializers.CharField( required = True)

class UserUpdatePasswordSerializer(serializers.Serializer):
    recovery_token = serializers.CharField(max_length = 200, required = True)
    new_password = serializers.CharField(max_length = 200, required = True)
