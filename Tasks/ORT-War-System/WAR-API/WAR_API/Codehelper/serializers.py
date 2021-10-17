from WAR_API import Codehelper
from rest_framework import serializers
from Users.models import Users
from Department.models import Department


class GetCodehelperSerializer(serializers.ModelSerializer):
    Department = serializers.CharField(source='Department.Username')
    CreatedBy = serializers.CharField(source='CreatedBy.StatusName')
    UpdatedBy = serializers.CharField(source='UpdatedBy.PriorityName')

    class Meta:
        model = Codehelper
        fields = "__all__"


class PostCodehelperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codehelper
        fields = "__all__"


# class GetLanguageSerializer(serializers.ModelSerializer)
