# Generated by Django 3.2 on 2021-05-04 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CodeHelper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Keyword', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('ProjectName', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=200)),
                ('FileUpload', models.FileField(blank=True, null=True, upload_to='file/')),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Codehelper.language')),
            ],
        ),
    ]