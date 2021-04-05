from django.db import models
from django.utils import timezone

# Create your models here.
gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

role_choices = [
    ('Web Developer', 'Web Developer'),
    ('Software Engineer', 'Software Engineer'),
    ('Software Tester', 'Software Tester'),
    ('Frontend Developer', 'Frontend Developer'),
    ('UI/UX Developer', 'UI/UX Developer'),
    ('Team Leader', 'Team Leader'),
    ('IOS Developer', 'IOS Developer'),
    ('Android Developer', 'Android Developer')
]


class Employee(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField()
    role = models.CharField(max_length=50, choices=role_choices, default='None', null=True, blank=True)
    DOB = models.DateField()
    email = models.EmailField()
    address = models.TextField()
    gender = models.CharField(max_length=15, choices=gender_choices, default='None', null=True, blank=True)
    profile_pic = models.ImageField(default='', blank=True, null=True)
    total_ctc = models.FloatField()
    joining_date = models.DateField(default=timezone.now().date())

    def __str__(self):
        return self.name



class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic = models.FloatField()
    DA = models.FloatField()
    HRA = models.FloatField()
    Conveyance = models.FloatField()
    Allowance = models.FloatField()
    Medical_Allowance = models.FloatField()
    other_earnings = models.FloatField()
    TDS = models.FloatField()
    ESI = models.FloatField()
    PF = models.FloatField()
    Leave = models.FloatField()
    Prof_Tax = models.FloatField()
    Labour_Welfare = models.FloatField()
    other_deductions = models.FloatField()
    net_salary = models.FloatField()
