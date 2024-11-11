from django.db import models
from .student import Student
from .subject import Subject
from .subject_group import SubjectGroup

class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_group = models.ForeignKey(SubjectGroup, on_delete=models.CASCADE)
    exam_1 = models.FloatField(null=True, blank=True)
    exam_2 = models.FloatField(null=True, blank=True)
    exam_3 = models.FloatField(null=True, blank=True)
    final_exam = models.FloatField(null=True, blank=True)
    final_grade = models.FloatField(null=True, blank=True)
    
