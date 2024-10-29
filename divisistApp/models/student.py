from django.db import models
from .user import User
from .career import Career

class Student(User):
    career = models.ForeignKey(Career, null=True, on_delete=models.SET_NULL)
    States = models.TextChoices('ACTIVO', 'INACTIVO')
    state = models.CharField(choices=States, max_length=20)
    