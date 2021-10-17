# Generated by Django 3.2 on 2021-05-04 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Department', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='DepartmentHead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept_head', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='TeamMembers',
            field=models.ManyToManyField(related_name='temam_members', to=settings.AUTH_USER_MODEL),
        ),
    ]