from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.
def demo(request):
    pass

def home(request):
    return render(request, 'accounts/login.html')

def content(request):
    return render(request, 'button.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('content')
            else:
                messages.info(request, "Username or Password is incorrect")

        context = {}
        return render(request, 'accounts/login.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("Username")
                p1 = form.cleaned_data.get("password1")
                p2 = form.cleaned_data.get("password2")
                if p1 == p2 :
                    print(user)
                    messages.success(
                        request, "Account was created for " + user)
                    return redirect('home')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
