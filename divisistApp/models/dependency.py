from django.db import models
from .staff import Staff

class Dependency(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, max_length=200)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
