from django.db import models
from .career import Career

class Subject(models.Model):

    career = models.ForeignKey(Career, on_delete=models.RESTRICT, primary_key=True)
    semester = models.IntegerField()
    consecutive = models.IntegerField()
    name = models.CharField(max_length=128)
    credits = models.IntegerField()
    hours = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['career', 'semester', 'consecutive'], name='unique_subject_code'),
        ]