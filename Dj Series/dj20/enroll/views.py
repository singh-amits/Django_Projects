from django.shortcuts import render
from enroll.forms import StudentRegistration

# Create your views here.
def showformdata(request):
    #fm = StudentRegistration(auto_id='some_%s')
    fm = StudentRegistration(auto_id=True, label_suffix='-', initial={ 'name':'Enter Your Name', 'email': 'Type Your Emil'})
    #fm.order_fields(field_order=None)
    #fm.order_fields(field_order=['email', 'name', 'first_name'])
    return render(request, 'enroll/userregistration.html', {'form': fm})
