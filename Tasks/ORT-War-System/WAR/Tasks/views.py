from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
# import requests

# Create your views here.a


def addtask(request):
    return render(request, 'tasks/addtask.html')


def displaytask(request):
    return render(request, 'tasks/displaytask.html')


def usertask(request):
    return render(request, 'tasks/displayusertask.html')
