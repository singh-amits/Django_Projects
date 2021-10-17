from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),

    # path('logout', v.logoutUser, name='logout'),

    path('home', v.home, name='home'),
    path('login', v.loginPage, name='login'),
    path('addemployee', v.addEmployee, name='addemployee'),
    path('displayemployee', v.displayemployee,
         name='displayemployee'),
    path('employeedetail', v.employeedetail, name='employeedetail')
]
