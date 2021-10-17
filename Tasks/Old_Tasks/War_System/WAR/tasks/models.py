from django.db import models
from Users.models import Employee
from Department.models import Department

     
from datetime import date
import datetime
my_date = datetime.date.today() 
year, week_num, day_of_week = my_date.isocalendar()

class Task(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('Active', 'Active'),
    )
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    Date = models.DateField(default=date.today(), blank=True)
    Day = models.CharField(default = day_of_week, max_length=10, choices=DAY_CHOICES)
    WeekNo = models.IntegerField(default=week_num)
    Task = models.CharField(max_length=200)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    Status = models.CharField(max_length=10, choices=STATUS, blank=True, null=True)


class ExpressModeTask(models.Model):
    Year = models.IntegerField(default = date.today().year)
    WeekNo = models.IntegerField(default=week_num)
    ExpProjectName = models.CharField(max_length=50)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Employee = models.ManyToManyField(Employee)


