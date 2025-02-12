from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10)

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    admission = models.OneToOneField('Admission', on_delete=models.CASCADE, related_name='student_admission')

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.CharField(max_length=100)
    total_marks = models.IntegerField()

class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='admission_record')
    date_of_admission = models.DateField()
    status = models.CharField(max_length=10)
