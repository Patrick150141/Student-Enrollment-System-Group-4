from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
date_of_birth = models.DateField()
address = models.CharField(max_length=255)
phone_number = models.CharField(max_length=15)
enrollment_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.user.username} - {self.user.get_full_name()}"



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Enrollment(models.Model):
     student = models.ForeignKey('Student', on_delete=models.CASCADE)
     course = models.ForeignKey('Course', on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('enrolled', 'Enrolled'), ('completed', 'Completed'), ('dropped', 'Dropped')])

    def __str__(self):
        return f"{self.student.user.username} - {self.course.title}"
    
    class Lecturer(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.user.get_full_name()}"
 
    class Grade(models.Model):
     enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    feedback = models.TextField()

    def __str__(self):
        return f"{self.enrollment.student.user.username} -{self.enrollment.course.title}"

