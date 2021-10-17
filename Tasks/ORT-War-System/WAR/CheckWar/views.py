from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
# import requests

# Create your views here.a


def warreport(request):
    return render(request, 'checkwar/warreport.html')


def warresult(request):
    return render(request, 'checkwar/warresult.html')
