# from django import forms
# from .models import Employee
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = Employee
#         fields = ['Username', 'password1','email','password2','is_staff','is_superuser','is_active','is_admin']
        
#         widgets = {
#             'Username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', }),
#             'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', }),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control','id': 'password1', }),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2', }),
#             'is_superuser': forms.CheckboxInput(attrs={"class": "check", 'id': 'superuser', 'type': 'checkbox', 'name': "isstaff"}),            
#             'is_staff': forms.CheckboxInput(attrs={"class": "check", 'id': 'staff', 'type': 'checkbox', 'name': "issuperuser"}),            
#             'is_active': forms.CheckboxInput(attrs={"class": "check", 'id': 'active', 'type': 'checkbox', 'name': "isactive"}),            
#             'is_admin': forms.CheckboxInput(attrs={"class": "check", 'id': 'admin', 'type': 'checkbox', 'name': "isadmin"}),            
#             }