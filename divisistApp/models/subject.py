from django.db import models
from .career import Career

class Subject(models.Model):
    
    career = models.ForeignKey(Career, on_delete=models.RESTRICT)
    consecutive = models.CharField(max_length=4)
    semester = models.SmallIntegerField()
    name = models.CharField(max_length=128)
    credits = models.SmallIntegerField()
    hours = models.SmallIntegerField()
    pensum = models.CharField(max_length=2)
    #listado de materias las cuales son pre-requisito para poder cursar la materia
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='required_for')
