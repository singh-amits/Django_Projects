from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Tododetail, name = "home" ),
    path("<int:id>/",views.update,name = 'update'),
    path('delete/<int:id>/',views.delete_data, name = "delete" ),
]
