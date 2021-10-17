from django.contrib import admin
from django.urls import path, include
from . import views as v
#from django.conf.urls import url
urlpatterns = [
    path('attendance', v.attendance, name='attendance'),

]
