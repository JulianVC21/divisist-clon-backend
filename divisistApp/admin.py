from django.contrib import admin
from .models import User, Student, Staff, Career, Faculty, Grades, Subject, Teacher, SubjectGroup

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Teacher)
admin.site.register(Career)
admin.site.register(Faculty)
admin.site.register(Grades)
admin.site.register(Subject)
admin.site.register(SubjectGroup)