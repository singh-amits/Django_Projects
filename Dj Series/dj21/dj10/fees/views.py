# Create your views here.
from django.shortcuts import render

def fees_django(request):
    return render(request, 'fees/info.html', {'nm': 'Django Fees'})