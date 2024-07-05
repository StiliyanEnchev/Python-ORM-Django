from django.db import models

# Creat e your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_in = models.DateTimeField(auto_now_add=True)


class Department(models.Model):

    class Location(models.TextChoices):
        VARNA = 'Varna', 'Varna'
        BURGAS = 'Burgas', 'Burgas'
        PLOVDIV = 'Plovidv', 'Plovdiv'
        SOFIA = 'Sofia', 'Sofia'

    code = models.CharField(
        max_length=4,
        primary_key=True,
        unique=True
    )
    name = models.CharField(
        max_length=50,
        unique=True
    )
    employees_count = models.PositiveIntegerField(
        default=1,
        verbose_name= 'Employees Count'
    )

    location = models.CharField(
        max_length=20,
        choices=Location,
        Null=True
    )
    last_edited_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
