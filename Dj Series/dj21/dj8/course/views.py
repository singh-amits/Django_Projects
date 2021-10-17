from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    #return HttpResponse("<h1>Hello Django</h1>")
    return render(request, 'courseone.html')
def learn_python(request):
    #return HttpResponse("<h1>Hello Python</h2>")
    return render(request, 'coursetwo.html')