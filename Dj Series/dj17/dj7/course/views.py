from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    a = '<h1>Hello Django</h1>'
    #return HttpResponse('hello Django')
    return HttpResponse(a)

def learn_python(request):
    return HttpResponse('hello Python')