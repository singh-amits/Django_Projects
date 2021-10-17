from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Department
from Users.models import Users

class DepartmentTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['Username']

class DepartmentSerializer(serializers.ModelSerializer):    
    CreatedBy = serializers.StringRelatedField()
    UpdatedBy = serializers.StringRelatedField()  
    DepartmentHead = serializers.StringRelatedField() 
    DepartmentTeam = DepartmentTeamSerializer(many = True, read_only = True)
    class Meta:
        model = Department
        fields = ['id','DepartmentName','DepartmentTeam','DepartmentHead', 'Active','CreatedBy','CreatedOn','UpdatedBy','UpdatedOn']

class DepartmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['DepartmentName','DepartmentTeam','DepartmentHead', 'Active','CreatedBy','CreatedOn','UpdatedBy','UpdatedOn']
   