from django.db import models
from .user import User
from .career import Career

class Student(User):
    consecutive = models.CharField(max_length=4, null=True)
    career = models.ForeignKey(Career, null=True, on_delete=models.RESTRICT)
    States = models.TextChoices('ACTIVO', 'INACTIVO')
    state = models.CharField(choices=States, max_length=20, default='ACTIVO')

    def save(self, *args, **kwargs):
        if not self.consecutive:  # Solo asignar el consecutivo si no se ha proporcionado
            # Contar cuántos estudiantes existen con la misma carrera
            student_count = Student.objects.filter(career=self.career).count()
            # Asignar el consecutivo como 1000 + el número de estudiantes
            self.consecutive = str(student_count + 1000)
        super().save(*args, **kwargs)
    