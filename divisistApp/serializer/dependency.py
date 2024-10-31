from rest_framework import serializers
from divisistApp.models import Dependency

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model=Dependency
        fields='__all__'
        