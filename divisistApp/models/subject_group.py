from django.db import models
from .subject import Subject


class SubjectGroup(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.RESTRICT)
    group = models.CharField(max_length=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['subject', 'group'], name='unique_subject_group_code'),
        ]
