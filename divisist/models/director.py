from user import User
from django.db import models

class Director(User):

    career = models.CharField()
    dependency = models.CharField()


    def Operation1(self, ):
        pass

    def getCareer(self, ):
        pass

    def setCareer(self, value):
        pass

    def getDependency(self, ):
        pass

    def setDependency(self, value):
        pass
