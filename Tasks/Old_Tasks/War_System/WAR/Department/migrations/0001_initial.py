# Generated by Django 3.2 on 2021-05-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepartmentCode', models.CharField(max_length=10)),
                ('DepartmentName', models.CharField(max_length=10)),
            ],
        ),
    ]
