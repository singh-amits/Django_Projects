# Generated by Django 3.2.1 on 2021-05-07 11:11

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
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DepartmentCreatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='UpdatedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DepartmentUpdatedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
