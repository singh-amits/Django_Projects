from django.db import models
from Users.models import Employee

class Department(models.Model):
    DepartmentCode = models.CharField(max_length=10)  
    DepartmentName = models.CharField(max_length=10)  
    DepartmentHead = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='dept_head')  
    TeamMembers = models.ManyToManyField(Employee, related_name='temam_members')
