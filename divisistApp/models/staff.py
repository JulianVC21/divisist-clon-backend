from django.db import models
from .user import User

class Staff(User):
    Positions = models.TextChoices('DIRECTIVO', 'DECANO')
    position = models.CharField(choices=Positions, max_length=10)