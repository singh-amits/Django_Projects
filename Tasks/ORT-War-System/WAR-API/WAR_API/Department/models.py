from django.db import models
from Users.models import Users
 
class Department(models.Model):
    DepartmentName = models.CharField(max_length=50, null=True)
    DepartmentTeam = models.ManyToManyField('Users.Users',null=True, blank=True)
    DepartmentHead = models.ForeignKey('Users.Users', on_delete=models.SET_NULL, related_name='DepartmentHead',null=True, blank=True)
    Active = models.BooleanField(default=False)
    CreatedBy = models.ForeignKey('Users.Users', on_delete=models.SET_NULL, related_name='DepartmentCreatedBy',null=True, blank=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey('Users.Users', on_delete=models.SET_NULL, null=True, blank=True, related_name='DepartmentUpdatedBy')
    UpdatedOn =  models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.DepartmentName