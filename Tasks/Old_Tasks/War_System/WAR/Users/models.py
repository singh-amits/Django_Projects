from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Designation(models.Model):
    Designation = models.CharField(max_length=30)

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
    def create_superuser(self,email, Username,password, is_staff=True, is_active=True,is_superuser=True):
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
        user.set_password(password)
        user.is_superuser= is_superuser
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    Username=models.CharField(max_length=20, unique=True)
    Fullname = models.CharField(max_length=50,null=True, blank=True)
    Address= models.CharField(max_length=100,null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    Designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.Username
