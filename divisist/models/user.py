from django.db import models

class User(models.Model):

    id = models.CharField()
    document = models.CharField()
    documentType = models.CharField()
    name = models.CharField()
    lastname = models.CharField()
    personalEmail = models.CharField()
    institutionalEmail = models.CharField()
    institutionalEmailPassword = models.CharField()
    birthday = models.DateField()
    phone = models.CharField()
    recoveryToken = models.CharField()

    def login(self, ):
        pass

    def generateRecoveryToken(self, ):
        pass

    def getName(self, ):
        pass

    def setName(self, value):
        pass

    def getLastname(self, ):
        pass

    def setLastname(self, value):
        pass

    def getPersonalEmail(self, ):
        pass

    def setPersonalEmail(self, value):
        pass

    def getInstitutionalEmail(self, ):
        pass

    def setInstitutionalEmail(self, value):
        pass

    def getInstitutionalEmailPassword(self, ):
        pass

    def setInstitutionalEmailPassword(self, value):
        pass

    def getBirthday(self, ):
        pass

    def setBirthday(self, value):
        pass

    def getPhoneNumbers(self, ):
        pass

    def setPhoneNumbers(self, value):
        pass

    def getRecoveryToken(self, ):
        pass

    def setRecoveryToken(self, ):
        pass

    def login(self, ):
        pass

    def recoverPassword(self, ):
        pass
