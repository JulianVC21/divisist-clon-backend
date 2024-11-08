from rest_framework import serializers
from divisistApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['dni', 'career', 'consecutive', 'password']

    def create(self, validated_data):
        raise NotImplementedError("Login does not create new students")

    def update(self, instance, validated_data):
        raise NotImplementedError("Login does not update students")