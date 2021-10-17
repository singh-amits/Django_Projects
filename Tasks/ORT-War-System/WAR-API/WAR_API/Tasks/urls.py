from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [
    path('taskList', v.taskList, name="taskList"),
    path('addNewTask', v.addNewTask, name="addNewTask"),
    path('deleteTask', v.deleteTask, name="deleteTask"),
    path('updateTask', v.updateTask, name="updateTask"),
]