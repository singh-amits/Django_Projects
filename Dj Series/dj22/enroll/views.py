from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('form validate')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('Name', name)
            print('Email', email)
            print('password', password)
            #fm = StudentRegistration()
            return render(request, 'enroll/success.html', {'nm': name})
        # print(fm)

    else:
        fm = StudentRegistration  # (auto_id=True, label_suffix='-', initial={
        # 'name': 'Enter Your Name', 'email': 'Type Your Email', 'mobile': 'Enter Mobile No.', })

    return render(request, 'enroll/userregistration.html', {'form': fm})
