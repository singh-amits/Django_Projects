from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
# import requests

# @login_required(login_url='login')


def home(request):
    return render(request, 'home.html')

# def loginPage(request):
#     # if request.user.is_authenticated:
#     #     return redirect('home')
#     # else:
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, "Username or Password is incorrect")
#     else:
#         context = {}
#         return render(request, 'accounts/login.html', context)


def loginPage(request):
    return render(request, 'accounts/login.html')


def addEmployee(request):
    return render(request, 'accounts/addemployee.html')


def employeedetail(request):
    return render(request, 'accounts/employeedetail.html')

# def addEmployee(request):
#     # if request.user.is_authenticated:
#     #     return redirect('home')
#     # else:
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get("Username")
#             p1 = form.cleaned_data.get("password1")
#             p2 = form.cleaned_data.get("password2")
#             if p1 == p2 :
#                 print(user)
#                 messages.success(
#                     request, "Account was created for " + user)
#                 return redirect('home')
#         else:
#             return render(request,'error.html', {'form':form})
#     else:
#         context = {'form': form}
#         return render(request, 'accounts/addEmployee.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('login')

def displayemployee(request):
    return render(request, 'accounts/displayemployee.html')
