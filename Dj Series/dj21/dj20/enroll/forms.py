from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Name", help_text="only 30 characters")
    # email = forms.EmailField()
    # first_name = forms.CharField()