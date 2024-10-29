from django.db import models
from .user import User

class Staff(User):
    Positions = models.TextChoices('directive', 'dean')
    position = models.CharField(choices=Positions, max_length=10)