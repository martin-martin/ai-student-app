from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)

    def __str__(self):
        return self.teacher_name

class ClassRoom(models.Model):
    class_room = models.CharField(max_length=20)

    def __str__(self):
        return self.class_room

class Member(models.Model):
    first_name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name

class Checkout(models.Model):
    student_name = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    checkout_choice = models.CharField(max_length=100)
    signature = models.TextField()
    checkout_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.checkout_time} -- ({self.checkout_choice}){self.student_name.first_name}'

