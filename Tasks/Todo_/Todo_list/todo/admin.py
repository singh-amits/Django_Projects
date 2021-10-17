from django.contrib import admin
from .models import task
# Register your models here.
@admin.register(task)
class taskadmin(admin.ModelAdmin):
    list_display = ("id", "Task_title")