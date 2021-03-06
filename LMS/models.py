from distutils.command.upload import upload
from email import message
from email.headerregistry import Address
import profile
from turtle import update
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.


class Claass(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)

class Customuser(AbstractUser):
    USER = (
        (1, 'PRINCIPAL'),
        (2, 'TEACHERS'),
        (3, 'STUDENTS'),
    )

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Teacher(models.Model):
    admin = models.OneToOneField(Customuser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username
#teacher = models.ForeignKey(Teacher,default='1', on_delete=models.CASCADE)

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # this will return name either the course object 1,2,3
        return self.name
    
class Session_Year(models.Model):
    session_start = models.CharField(max_length=80)
    session_end = models.CharField(max_length=80)

    def __str__(self):
        return self.session_start + " To " + self.session_end


class Student(models.Model):
    admin = models.OneToOneField(Customuser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name



class Teacher_Notification(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.teacher_id.admin.first_name


class Teacher_leave(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    data = models.CharField(max_length=80)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacher_id.admin.first_name + self.teacher_id.admin.last_name


class Student_Leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    data = models.CharField(max_length=80)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name


class Attendance(models.Model):
    course_id = models.ForeignKey(Course, null=True, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_id.name

class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name


class Student_Result(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_marks = models.IntegerField()
    presentation_marks = models.IntegerField()
    exam_marks = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name