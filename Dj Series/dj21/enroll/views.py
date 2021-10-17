from django.shortcuts import render
from enroll.forms import StudentRegistration

# Create your views here.
def showformdata(request):
    fm = StudentRegistration(auto_id=True, label_suffix='-', initial={ 'name':'Enter Your Name', 'email': 'Type Your Email', 'mobile':'Enter Mobile No.',})
    return render(request, 'enroll/userregistration.html', {'form': fm})
