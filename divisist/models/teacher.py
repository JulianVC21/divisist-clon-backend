from user import User
from django.db import models

class Teacher(User):
    class Meta:
        pass

    career = models.CharField()
    subjects = models.JSONField()


    def getId(self, ):
        pass

    def setId(self, value):
        pass

    def getCareer(self, ):
        pass

    def setCareer(self, value):
        pass

    def getSubjects(self, ):
        pass

    def setSubjects(self, value):
        pass

    def setNote(self, subject, student, note):
        pass