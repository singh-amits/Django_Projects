from Department.models import Department
from rest_framework import serializers
from .models import Project
#from Department.models import Department


class GetProjectSerializer(serializers.ModelSerializer):
    CreatedBy = serializers.CharField(source='CreatedBy.Username')
    UpdatedBy = serializers.CharField(source='UpdatedBy.Username')
    BA = serializers.CharField(source='BA.Username')
    Department = serializers.CharField(source='Department.Username')
    ProjectHead = serializers.CharField(source='ProjectHead.Username')

    class Meta:
        model = Project
        fields = "__all__"


class PostProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
