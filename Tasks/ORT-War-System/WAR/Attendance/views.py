from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
# import requests

# Create your views here.


def attendance(request):
    return render(request, 'attendance/attendance.html')
