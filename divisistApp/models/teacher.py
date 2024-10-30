from django.db import models
from. user import User

class Teacher(User):

    consecutive = models.CharField(max_length=6, unique=True)