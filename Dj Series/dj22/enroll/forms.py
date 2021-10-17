from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()  # (label='Your Name', label_suffix=' ',
    # initial='Amit', required=False, disabled=True, help_text='70')
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
