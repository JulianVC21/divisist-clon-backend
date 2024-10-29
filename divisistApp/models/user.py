from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null= False)
    personal_email = models.EmailField(max_length=200 ,null=False, unique=True)
    institutional_email = models.EmailField(max_length=200 ,null=False, unique=True)
    institutional_email_password = models.CharField(max_length=200 ,null=False)
    birthday = models.DateField()
    recovery_token = models.CharField(max_length=200 ,null=True, unique=True)

    def login(self, ):
        pass

    def generate_recovery_token(self, ):
        pass

    def get_name(self, ):
        pass

    def set_name(self, value):
        pass

    def get_last_name(self, ):
        pass

    def set_last_name(self, value):
        pass

    def get_personal_mail(self, ):
        pass

    def set_personal_mail(self, value):
        pass

    def get_institutional_email(self, ):
        pass

    def set_institutional_email(self, value):
        pass

    def get_institutional_email_password(self, ):
        pass

    def set_institutional_email_password(self, value):
        pass

    def get_birthday(self, ):
        pass

    def set_birthday(self, value):
        pass

    def get_phone_numbers(self, ):
        pass

    def set_phone_numbers(self, value):
        pass

    def get_recovery_token(self, ):
        pass

    def set_recovery_token(self, ):
        pass

    def login(self, ):
        pass

    def recover_password(self, ):
        pass
