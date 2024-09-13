import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self) -> str:
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Department"
        verbose_name = "Department"
        verbose_name_plural = "Departments"


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    hire_date = models.DateField()
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees'
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'Employee'
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


class Project(models.Model):
    name = models.CharField(max_length=150)
    employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.employee

    class Meta:
        db_table = "EmployeeProfile"
        verbose_name = "Employee Profile"
        verbose_name_plural = "Employee Profiles"
