from rest_framework import serializers
from .models import TaskMaster
from Users.models import Users


class AssignToSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['Username']


class GetTaskMasterSerializer(serializers.ModelSerializer):
    AssignBy = serializers.CharField(source='AssignBy.Username')
    Status = serializers.CharField(source='Status.StatusName')
    TaskPriority = serializers.CharField(source='TaskPriority.PriorityName')
    CreatedBy = serializers.CharField(source='CreatedBy.Username')
    UpdatedBy = serializers.CharField(source='UpdatedBy.Username')
    AssignTo = AssignToSerializer(many=True, read_only=True)
    AssignTo = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TaskMaster
        fields = "__all__"


class PostTaskMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMaster
        fields = "__all__"
