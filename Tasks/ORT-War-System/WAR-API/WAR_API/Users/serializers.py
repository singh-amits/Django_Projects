from rest_framework import serializers
from .models import Designation, Role, Users, ErrorLog, LevelMaster, UserToManager


class UserSerializer(serializers.ModelSerializer):
    DesignationId = serializers.StringRelatedField()
    DepartmentID = serializers.StringRelatedField()
    RoleID = serializers.StringRelatedField()
    # CreatedBy = serializers.
    # UpdatedBy = serializers.StringRelatedField()

    class Meta:
        model = Users
        fields = ['id', 'Username', 'Fullname', 'Address', 'Gender', 'email', 'DesignationId', 'Photo', 'RoleID', 'DepartmentID', 'Phone',
                  'FirebaseID', 'CreatedBy', 'CreatedOn', 'UpdatedBy', 'UpdatedOn', 'is_staff', 'is_superuser', 'is_active', 'is_admin']


class userRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['Username', 'password', 'Password', 'Fullname', 'Address', 'Gender', 'email', 'DesignationId', 'Photo', 'RoleID', 'DepartmentID', 'Phone',
                  'FirebaseID', 'CreatedBy', 'CreatedOn', 'UpdatedBy', 'UpdatedOn', 'is_staff', 'is_superuser', 'is_active', 'is_admin']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = Users(
            Username=self.validated_data['Username'],
            Fullname=self.validated_data['Fullname'],
            Address=self.validated_data['Address'],
            Gender=self.validated_data['Gender'],
            email=self.validated_data['email'],
            DesignationId=self.validated_data['DesignationId'],
            Photo=self.validated_data['Photo'],
            RoleID=self.validated_data['RoleID'],
            DepartmentID=self.validated_data['DepartmentID'],
            Phone=self.validated_data['Phone'],
            is_staff=self.validated_data['is_staff'],
            is_superuser=self.validated_data['is_superuser'],
            is_active=self.validated_data['is_active'],
            is_admin=self.validated_data['is_admin'],
            Password=self.validated_data['password']

        )

        password = self.validated_data['password']
        # password = self.context['request'].data['password']
        user.set_password(password)
        user.CreatedBy = self.context['request'].user
        user.save()
        return user


class userUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['Username', 'password', 'Password', 'Fullname', 'Address', 'Gender', 'email', 'DesignationId', 'Photo', 'RoleID', 'DepartmentID', 'Phone',
                  'FirebaseID', 'CreatedBy', 'CreatedOn', 'UpdatedBy', 'UpdatedOn', 'is_staff', 'is_superuser', 'is_active', 'is_admin']
