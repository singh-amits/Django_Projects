# Generated by Django 3.2.1 on 2021-05-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_remove_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
