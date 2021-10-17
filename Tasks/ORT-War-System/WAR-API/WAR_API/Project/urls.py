from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [
    path('projectList', v.projectList, name="projectList"),
    path('addNewProject', v.addNewProject, name="addNewProject"),
    path('deleteProject', v.deleteProject, name="deleteProject"),
    path('updateProject', v.updateProject, name="updateProject"),
]
