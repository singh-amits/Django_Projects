from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
# import requests

# Create your views here.a


def project(request):
    return render(request, 'project/newproject.html')


def displaydept(request):
    return render(request, 'project/displaydept.html')


def displayba(request):
    return render(request, 'project/displayba.html')
