from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dept', v.department, name='department'),
    path('deptdetail', v.deptdetail, name='deptdetail'),

]
