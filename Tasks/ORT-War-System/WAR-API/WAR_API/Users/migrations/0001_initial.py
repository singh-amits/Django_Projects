# Generated by Django 3.2.1 on 2021-05-07 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Department', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DesignationName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LevelMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LevelName', models.CharField(max_length=20)),
                ('Active', models.BooleanField(default=False)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoleName', models.CharField(max_length=20)),
                ('Active', models.BooleanField(default=False)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Username', models.CharField(max_length=20, unique=True)),
                ('Fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('Password', models.CharField(max_length=50)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1, null=True)),
                ('Email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('Photo', models.FileField(blank=True, null=True, upload_to='profileImages/')),
                ('Phone', models.CharField(blank=True, max_length=10, null=True)),
                ('FirebaseID', models.CharField(blank=True, max_length=100, null=True)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('DepartmentID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Department.department')),
                ('DesignationId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.designation')),
                ('RoleID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.role')),
                ('UpdatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserUpdatedBy', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserToManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Active', models.BooleanField(default=False)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserManagerMappingCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('LevelID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.levelmaster')),
                ('ManagerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ManagerID', to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserManagerMappingUpdatedBy', to=settings.AUTH_USER_MODEL)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RoleCreatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='role',
            name='UpdatedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RoleUpdatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='levelmaster',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LevelCreatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='levelmaster',
            name='DepartmentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Department.department'),
        ),
        migrations.AddField(
            model_name='levelmaster',
            name='UpdatedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LevelUpdatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExceptionMsg', models.TextField(null=True)),
                ('ExceptionType', models.TextField(null=True)),
                ('ExceptionSource', models.TextField(null=True)),
                ('ExceptionUrl', models.CharField(max_length=500, null=True)),
                ('ActionName', models.CharField(max_length=500, null=True)),
                ('IPAddress', models.CharField(max_length=500, null=True)),
                ('LogDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('ControllerName', models.CharField(max_length=500, null=True)),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]