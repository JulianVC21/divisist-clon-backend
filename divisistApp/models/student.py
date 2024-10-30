from django.db import models
from .user import User
from .career import Career

class Student(User):
    consecutive = models.CharField(max_length=4, null=True)
    career = models.ForeignKey(Career, null=True, on_delete=models.RESTRICT)
    States = models.TextChoices('ACTIVO', 'INACTIVO')
    state = models.CharField(choices=States, max_length=20, default='ACTIVO')

    