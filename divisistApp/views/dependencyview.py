from rest_framework import viewsets
from divisistApp.serializer import DependencySerializer
from divisistApp.models import Dependency

class DependencyViewSet(viewsets.ModelViewSet):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer