from django.db import models
from .student import Student
from .subject_group import SubjectGroup

class Grades(models.Model):

    subject = models.ForeignKey(SubjectGroup, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    first_exam = models.DecimalField(max_digits=1, decimal_places=1, null=True)
    second_exam = models.DecimalField(max_digits=1, decimal_places=1, null=True)
    third_exam = models.DecimalField(max_digits=1, decimal_places=1, null=True)
    final_exam = models.DecimalField(max_digits=1, decimal_places=1, null=True)
    