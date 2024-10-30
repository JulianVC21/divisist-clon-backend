from django.db import models
from .subject import Subject
from .teacher import Teacher

class SubjectGroup(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.RESTRICT)
    group = models.CharField(max_length=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    academic_year = models.CharField(max_length=7)
    max_capacity = models.SmallIntegerField()
