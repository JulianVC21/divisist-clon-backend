from user import User
from django.db import models

class Student(User):
    class Meta:
        pass

    career = models.CharField()
    actualSemester =models.IntegerField()
    creditsApproved = models.IntegerField()
    enrolledSubjects = models.JSONField()


    def getCareer(self, ):
        pass

    def setCareer(self, value):
        pass

    def getActualSemester(self, ):
        pass

    def setActualSemester(self, value):
        pass

    def getCreditsApproved(self, ):
        pass

    def setCreditsApproved(self, value):
        pass

    def getEnrolledSubjects(self, ):
        pass

    def setEnrolledSubjects(self, value):
        pass
