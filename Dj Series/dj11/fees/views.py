from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/feesone.html', {'title': 'DJango Fees', 'cname': 'Django', 'charge': 300})