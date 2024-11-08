from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null= False)
    personal_email = models.EmailField(max_length=200 ,null=False, unique=True)
    dni = models.CharField(max_length=12, unique=True, default='0')
    password = models.CharField(max_length=200, null=True)
    institutional_email = models.EmailField(max_length=200 ,null=False, unique=True)
    birthday = models.DateField(null=False)
    recovery_token = models.CharField(max_length=200 ,null=True, unique=True)

    def save(self, *args, **kwargs):
        # Solo encripta la contraseña si aún no ha sido encriptada
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password) 
