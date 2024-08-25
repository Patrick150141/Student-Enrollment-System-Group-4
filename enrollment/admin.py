from django.contrib import admin
from .models import Course, Student,Enrollment,Grade,Lecturer
 
 
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(Lecturer)