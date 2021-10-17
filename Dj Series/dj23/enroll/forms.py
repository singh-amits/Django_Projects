from django.core import validators
from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()  # (label='Your Name', label_suffix=' ',
    # initial='Amit', required=False, disabled=True, help_text='70')
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)


def clean_name(self):
    valname = self.cleaned_data['name']
    if len(valname) < 4:
        raise forms.ValidationError('Enter more than 4 digit')
    return valname
