from django import forms
from .models import task

class Task_assign(forms.ModelForm):

    class Meta:
        forms.DateTimeInput.input_type ="datetime-local"
        model = task
        fields = ['Task_title','Task_img','description','description_img','deadline']
        widgets = {
            'Task_title': forms.TextInput(attrs = {'class' : "form-control"}),
            'description' : forms.TextInput(attrs = {'class' : "form-control"}),
            'deadline' : forms.DateTimeInput()
        }         
        
        #    'Task_img' : forms.ImageField(),
        #     'discription_img': forms.ImageField(),
