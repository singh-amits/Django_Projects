from django.contrib import admin
from django.urls import path, include
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', v.home, name='home'),
    path('login', v.loginPage, name='login'),
    path('content', v.content, name='content'),
    path('register', v.registerPage, name='register'),
    path('logout', v.logoutUser, name='logout'),
]
