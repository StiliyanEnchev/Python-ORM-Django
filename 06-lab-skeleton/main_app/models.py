from datetime import datetime, date

from django.db import models


class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    lecturer = models.ForeignKey(Lecturer,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 )

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    subjects = models.ManyToManyField(Subject, through='StudentEnrollment')


class StudentEnrollment(models.Model):

    class StudentGrades(models.TextChoices):
        A = "A", "A"
        B = "B", "B"
        C = "C", "C"
        E = "E", "E"
        D = "D", "D"
        F = "F", "F"

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=StudentGrades)
    enrollment_date = models.DateField(default=date.today)


class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(Lecturer, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    office_location =models.CharField(max_length=100, null=True, blank=True)