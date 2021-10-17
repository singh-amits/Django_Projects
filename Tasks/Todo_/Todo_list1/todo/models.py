from django.db import models

# Create your models here.
class task(models.Model):
    id = models.AutoField(primary_key=True)

    Task_title = models.CharField(max_length = 50,null = True)
    Task_img = models.ImageField(upload_to = "images/", max_length = 255)
    description = models.CharField(max_length = 70,null = True)
    description_img = models.ImageField(upload_to = "images/", max_length = 255)
    date_joined = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    