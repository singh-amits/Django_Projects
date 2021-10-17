from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.forms import Form
from .models import CustomUser


class NewUserForm(UserCreationForm):
    """
    Custom form for user creation
    Takes username, email and password as inputs
    """
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        #remove help tex from form
        for fieldname in ["username", "email", "password1", "password2"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        """
        Checks if email already resgistered with an account
        """
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email):
            raise forms.ValidationError(("E-mail already registered with an account"))
        return email

    def clean_password2(self):
        """
        Checks if passwords match
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    ("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class OTPVerificationForm(forms.Form):
    user_otp = forms.IntegerField(required=True)
