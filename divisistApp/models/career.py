from django.db import models
from .faculty import Faculty
from .staff import Staff

class Career(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=200, unique=True)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    active_pensum = models.CharField(max_length=2, null=True)
