from django.db import models
from django.contrib.auth.models import User




class Student (models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attendance (models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent')
        ]
    )

    def __str__(self):
        return f"{self.student.name} - {self.date}"
    

# Create your models here.
class UserSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username