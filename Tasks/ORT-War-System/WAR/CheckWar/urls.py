from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [

    path('warreport', v.warreport, name='warreport'),
    path('warresult', v.warresult, name='warresult'),
]
