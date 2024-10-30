from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null= False)
    personal_email = models.EmailField(max_length=200 ,null=False, unique=True)
    dni = models.CharField(max_length=12, unique=True, null=True)
    password = models.CharField(max_length=200, null=True)
    institutional_email = models.EmailField(max_length=200 ,null=False, unique=True)
    birthday = models.DateField()
    recovery_token = models.CharField(max_length=200 ,null=True, unique=True)
