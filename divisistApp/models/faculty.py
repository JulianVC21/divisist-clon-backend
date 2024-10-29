from django.db import models
from .staff import Staff

class Faculty(models.Model):

    name = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    dean = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
