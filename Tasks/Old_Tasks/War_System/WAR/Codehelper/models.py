from django.db import models

class Language(models.Model):
    Language = models.CharField(max_length=50)

class CodeHelper(models.Model):
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    Keyword = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    ProjectName = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    FileUpload = models.FileField(upload_to='file/', blank=True, null=True)
