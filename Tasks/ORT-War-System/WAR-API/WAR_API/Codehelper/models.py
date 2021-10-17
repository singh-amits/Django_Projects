from django.db import models
from Users.models import Users
from Department.models import Department


import datetime
my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()
week = week_num
year_num = year
day = day_of_week


class Codehelper(models.Model):
    Language = models.CharField(max_length=100, null=True)
    KeyWord = models.CharField(max_length=1000, null=True)
    Title = models.CharField(max_length=500, null=True)
    Description = models.DateTimeField(null=True)
    FileUpload = models.DateTimeField(null=True)
    UploadedBy = models.CharField(max_length=500, null=True)
    Department = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='department', null=True, blank=True)
    ProjectName = models.CharField(max_length=200, null=True)
    #Team = models.CharField(max_length=1000, null=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField(default=False)
    CreatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='codecreatedby', null=True, blank=True)
    UpdatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='codeupdatedby', null=True, blank=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True, blank=True)


# #class Language(models.Model):
#     Language = models.CharField(max_length=100, null=True)
