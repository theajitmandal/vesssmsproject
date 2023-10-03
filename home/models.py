from django.db import models


# Create your models here.

class ClassName(models.Model):
    classname = models.CharField(max_length=100)

    def __str__(self):
        return self.classname

class Subject(models.Model):
    subjectname = models.CharField(max_length=100)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)

    def __str__(self):
        return self.subjectname

class Teacher(models.Model):
    name = models.CharField(max_length=500)
    gmail = models.EmailField()
    gender = models.CharField(max_length=50, default="male")
    address = models.TextField()
    phone = models.CharField(max_length=800)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=500)
    gmail = models.EmailField()
    gender = models.CharField(max_length=50, default="male")
    address = models.TextField()
    phone = models.CharField(max_length=800)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    obtainedmark = models.DecimalField(max_digits=6, decimal_places=2)

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

