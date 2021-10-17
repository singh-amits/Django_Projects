from django.contrib import admin
from django.urls import path, include
from . import views as v
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    
    

    path('home', v.home, name='home'),
    path('api/login', v.login, name='login'),
    path('api/logout', v.logout, name='logout'),
    path('addemployee', v.addEmployee, name='addEmployee'),

    # API - User - userlist
    path('api/userlist',v.UserListAPI, name = 'userlistapi'),
    path('api/adduser', v.addUser, name = 'addUser'),
    path('api/userdelete', v.userDelete, name = 'userdelete'),
    path('api/userupdate', v.userUpdate, name = 'userupdate'),

]
