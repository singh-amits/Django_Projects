from django.db import models
from Users.models import Users

import datetime
my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()
week = week_num
year_num = year
day = day_of_week


class Status(models.Model):
    StatusName = models.CharField(max_length=25)  # Pending, completed, reopen

    def __str__(self):
        return self.StatusName


class TaskPriorityMaster(models.Model):
    PriorityName = models.CharField(max_length=25)  # high, medium, low

    def __str__(self):
        return self.PriorityName


class TaskMaster(models.Model):
    AssignTo = models.ManyToManyField(
        Users, blank=True, related_name='assignto')
    AssignBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='assignby', null=True, blank=True)
    AssignDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Status = models.ForeignKey(
        Status, on_delete=models.CASCADE, null=True, blank=True)
    Week = models.IntegerField(default=week, null=True)
    TaskTitle = models.CharField(max_length=50)
    TaskDescription = models.CharField(max_length=500, null=True)
    DueDateTime = models.DateField(null=True)
    TaskPriority = models.ForeignKey(
        TaskPriorityMaster, on_delete=models.CASCADE, null=True, blank=True)
    Active = models.BooleanField(default=False)
    CreatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='createdby', null=True, blank=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='updatedby', null=True, blank=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.TaskTitle


class NotificationTypeMaster(models.Model):
    Type = models.CharField(max_length=50)  # InApp, Firebase, SMS

    def __str__(self):
        return self.Type


class TaskNotification(models.Model):
    NotificationTitle = models.CharField(max_length=50)
    NotificationMsg = models.CharField(max_length=500, null=True)
    UserID = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='idUser', null=True, blank=True)
    ReadMsg = models.BooleanField(default=False)
    NotificationTypeId = models.ForeignKey(
        NotificationTypeMaster, on_delete=models.CASCADE)
    CreatedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NotificationTitle
