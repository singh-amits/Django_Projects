from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_django(request):
    return render(request, 'feesone.html')
    #return HttpResponse("<h1>3000</h1>")

def fees_python(request):
    #return HttpResponse("<h1>2000</h2>")
    return render(request, 'feestwo.html')
# Create your views here.
