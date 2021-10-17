from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
# import requests

# Create your views here.a


def department(request):
    return render(request, 'department/department.html')


def deptdetail(request):
    return render(request, 'department/deptdetail.html')
