from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def fees_django(request):
 #   return HttpResponse("<h1> Django - 300</h1>")

#def fees_python(request):
 #   return HttpResponse("<h1> Python - 500</h1>")
# Create your views here.
def fees_django(request):
    return render(request, 'fees/feesone.html')
def fees_python(request):
    return render(request, 'templates/fees/feestwo.html')