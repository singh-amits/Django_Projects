from django.db import models
from Department.models import Department
from Users.models import Users


import datetime
my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()
week = week_num
year_num = year
day = day_of_week


class Project(models.Model):
    ProjectCode = models.CharField(max_length=100, null=True)
    ProjectName = models.CharField(max_length=1000, null=True)
    ClientName = models.CharField(max_length=500, null=True)
    StartDate = models.DateField(auto_now_add=True)
    TargetDate = models.DateField(null=True)
    BA = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='projectba', null=True, blank=True)
    Department = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='projectdepartment', null=True, blank=True)
    ProjectHead = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='projecthead', null=True, blank=True)
    #Team = models.CharField(max_length=1000, null=True)
    Status = models.IntegerField(null=True)
    Active = models.BooleanField(default=False)
    CreatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='projectcreatedby', null=True, blank=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='projectupdatedby', null=True, blank=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.ProjectName


# class Timeline(models.Model):
#     ProjectCode = models.CharField(max_length=100, null=True)
#     M_date = models.DateField(auto_now_add=True, null=True, blank=True)
#     Msg = models.CharField(max_length=1000, null=True)
#     UserName = models.CharField(max_length=20, null=True)
