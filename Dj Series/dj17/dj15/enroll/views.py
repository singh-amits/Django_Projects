from django.shortcuts import render
from enroll.models import Student

def studentinfo(request):
 stud = Student.objects.all()
 print('Myoutput', stud)
 return render(request, 'enroll/studetails.html', {'stu': stud})

    
