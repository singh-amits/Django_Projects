import pyotp
from django.core.exceptions import ValidationError
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.views.generic.base import RedirectView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import cache_control, never_cache
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import NewUserForm, OTPVerificationForm
from .models import CustomUser
from quiz.models import UserProgress
from QuizApp.settings import EMAIL_HOST_USER

# Create your views here.

class HomePageView(TemplateView):
    """
    Index page.
    Displays pending quizzes for logged in users, if any.
    """
    template_name = "userauth/home.html"

    def dispatch(self, request, *args, **kwargs):        
        self.logged_in_user = self.request.user.is_authenticated

        if self.logged_in_user:
            try:
                #check for incomplete quizzes
                incomplete_quiz = UserProgress.objects.filter(user=request.user, complete=False)
                kwargs['incomplete_quiz'] = [obj.quiz for obj in incomplete_quiz if obj]
            except UserProgress.DoesNotExist:
                pass               
                                              
        return super(HomePageView, self).dispatch(request, *args, **kwargs)


@method_decorator(never_cache, 'dispatch')
class OTPVerificationView(generic.View):

    """
    OTP verification view.
    Gets sent otp and user data from session.
    Checks for correct otp, creates and log the user in.
    Delete session data.
    """

    form_class = OTPVerificationForm
    template = 'userauth/otp.html'

    def get(self, *args, **kwargs):
        otp = self.request.session.get('otp', None)
        if otp is None:
            return redirect('userauth:register')
        form = self.form_class()
        return render(self.request, self.template, {'form': form})

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)

        if form.is_valid():
            user_otp = form.cleaned_data.get('user_otp')
            otp = self.request.session.get('otp', None)
            user = self.request.session['username']
            hash_pwd = make_password(self.request.session.get('password'))
            email_address = self.request.session.get('email') 
            #compare otp
            if int(user_otp) != int(otp):
                messages.error(self.request, "Incorrect otp, try again")
                return render(self.request, self.template,{'form': form})
            
            new_user = CustomUser.objects.create(
                                username = user,
                                email=email_address,
                                password=hash_pwd
                )
            new_user.save()
            new_user.is_active=True
            #delete session data
            self.request.session.delete('otp')
            self.request.session.delete('user')
            self.request.session.delete('email')
            self.request.session.delete('password')
            self.request.session.delete('phone_number')
            messages.success(self.request,'Registration Successfully Done !!')
            #log in user
            login(self.request,new_user)
    
        else:
            raise ValidationError('Incorrect otp')
        return redirect('userauth:homepage')


class RegisterView(FormView):

    """
    Registration page to register new user.
    Takes username, email and password as input and send an otp via email.
    Redirects to otp verification page
    """

    form_class = NewUserForm
    template_name = 'userauth/register.html'

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        base32 = pyotp.random_base32()
        totp = pyotp.TOTP(base32)
        otp = totp.now()
        self.request.session['email'] = email
        self.request.session['username'] = username
        self.request.session['password'] = password
        self.request.session['otp'] = otp
        subject = 'QuizApp Email Verification'
            
        message = 'Your OTP is : '+str(otp)
        recepient = str(form.cleaned_data.get('email'))
        send_mail(subject, message, EMAIL_HOST_USER,
                [recepient], fail_silently=False)
        return redirect('userauth:otp')

    def form_invalid(self, form):
        errors = form.errors.as_data()
        for msg in errors:
            error = ''.join(map(str, errors[msg][0]))
            messages.error(self.request, f"{error}")
        return super().form_invalid(form)


class LogoutView(RedirectView):

    """
    Logs out user and redirects user to homepage
    """
    url = '/'

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class LoginView(FormView):

    """
    Login form for registered users.
    Takes username and password as parameters
    """
    
    form_class = AuthenticationForm
    template_name = 'userauth/login.html'

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.info(self.request, f"You are now logged in as {username}")
            return redirect('/')
        else:
            messages.error(self.request, "Invalid username or password.")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)