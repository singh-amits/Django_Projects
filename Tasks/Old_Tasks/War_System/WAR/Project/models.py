from django.db import models

from datetime import date
import datetime
my_date = datetime.date.today() 
year, week_num, day_of_week = my_date.isocalendar()

from Users.models import Employee
from Department.models import Department

class Project(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('Active', 'Active'),
    )
    ProjectCode = models.CharField(max_length=10)
    ProjectName =  models.CharField(max_length=50)
    ClientName =  models.CharField(max_length=50)
    StartDate = models.DateField(default=date.today(), blank=True)
    TargetDate = models.DateField( blank=True, null=True)
    BusinessAnalyst = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='business_analyst')  
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    ProjectHead = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='project_head')  
    TeamMembers = models.ManyToManyField(Employee, related_name='team_members')
    Status =  models.CharField(max_length=10, choices=STATUS, blank=True, null=True)
