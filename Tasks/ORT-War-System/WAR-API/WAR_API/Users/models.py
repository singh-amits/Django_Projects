from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Designation(models.Model):
    DesignationName = models.CharField(max_length=30)

    def __str__(self):
        return self.DesignationName


class Role(models.Model):
    RoleName = models.CharField(max_length=20)
    Active = models.BooleanField(default=False)
    CreatedBy = models.ForeignKey(
        'Users', on_delete=models.CASCADE, related_name='RoleCreatedBy')
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(
        'Users', on_delete=models.CASCADE, null=True, blank=True, related_name='RoleUpdatedBy')
    # will get updated everytime model is saved
    UpdatedOn = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.RoleName


class CustomUserManager(BaseUserManager):
    def create_user(self, email, Username, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not Username:
            raise ValueError("User must have a Username")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.Username = Username
        user.set_password(password)  # change password to hash
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, Username, password, is_staff=True, is_active=True, is_superuser=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not Username:
            raise ValueError("User must have a Username")

        user = self.model(
            email=self.normalize_email(email)
        )
        # other_fields.setdefault('is_staff', True)
        # other_fields.setdefault('is_superuser', True)
        # other_fields.setdefault('is_active', True)

        # if other_fields.get('is_staff') is not True:
        #     raise ValueError(
        #         'Superuser must be assigned to is_staff=True.')
        # if other_fields.get('is_superuser') is not True:
        #     raise ValueError(
        #         'Superuser must be assigned to is_superuser=True.')

        user.Username = Username
        user.set_password(password)
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user

        # return self.create_user(email, password, **other_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    Username = models.CharField(max_length=20, unique=True)
    Fullname = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    DesignationId = models.ForeignKey(
        Designation, on_delete=models.CASCADE, null=True, blank=True)
    Photo = models.FileField(upload_to='profileImages/', null=True, blank=True)
    RoleID = models.ForeignKey(
        Role, on_delete=models.SET_NULL,  null=True, blank=True)
    DepartmentID = models.ForeignKey(
        'Department.Department', on_delete=models.CASCADE, null=True, blank=True)
    Phone = models.CharField(max_length=10, null=True, blank=True)
    FirebaseID = models.CharField(max_length=100, null=True, blank=True)
    CreatedBy = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name='UserCreatedBy', null=True, blank=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name='UserUpdatedBy', null=True, blank=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.Username + ' (' + str(self.DesignationId) + ') ' + ' (' + str(self.DepartmentID) + ') '


class ErrorLog(models.Model):
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE)
    ExceptionMsg = models.TextField(null=True)
    ExceptionType = models.TextField(null=True)
    ExceptionSource = models.TextField(null=True)
    ExceptionUrl = models.CharField(max_length=500, null=True)
    ActionName = models.CharField(max_length=500, null=True)
    IPAddress = models.CharField(max_length=500, null=True)
    LogDate = models.DateTimeField(auto_now_add=True, null=True)
    ControllerName = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.ExceptionMsg


class LevelMaster(models.Model):
    LevelName = models.CharField(max_length=20)
    DepartmentID = models.ForeignKey(
        'Department.Department', on_delete=models.CASCADE)  # .....doubt
    Active = models.BooleanField(default=False)
    CreatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='LevelCreatedBy')
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True, blank=True, related_name='LevelUpdatedBy')
    UpdatedOn = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return 'Level ' + str(self.LevelName) + ' ' + str(self.DepartmentID)


class UserToManager(models.Model):
    UserID = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='UserID')
    ManagerID = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='ManagerID')
    LevelID = models.ForeignKey(LevelMaster, on_delete=models.CASCADE)
    Active = models.BooleanField(default=False)
    CreatedBy = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='UserManagerMappingCreatedBy')
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(Users, on_delete=models.CASCADE,
                                  null=True, blank=True, related_name='UserManagerMappingUpdatedBy')
    UpdatedOn = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.UserID) + ' reports to ' + str(self.ManagerID) + '(Level ' + str(self.LevelID) + ')'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
