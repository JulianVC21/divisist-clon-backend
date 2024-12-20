from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'dependencies', views.DependencyViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]