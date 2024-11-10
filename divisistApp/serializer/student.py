from rest_framework import serializers
from divisistApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        extra_kwargs = {
            'state': {'read_only': True},
            'consecutive': {'read_only': True},
            'recovery_token': {'read_only': True},
        }

class StudentLoginSerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=20)
    career = serializers.CharField(max_length=100)
    consecutive = serializers.CharField(max_length=10)
    password = serializers.CharField(write_only=True, max_length=100)