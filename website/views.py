from django.shortcuts import render, redirect

# django authentication login system
from django.contrib.auth import authenticate, login, logout

# pop up messages
from django.contrib import messages

from .forms import SignUpForm
# Create your views here.

def home(request):
    # Check if logging in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logg In Completed Successfully!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error While Logging In. \nPlease Try Again.")
            return redirect('home')
    else:       
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    """
    Log out option should appear in the nav bar only if the 
    user is actually logged in
    """
    logout(request)
    messages.success(request, "User Logged Out")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)

            login(request, user)
            messages.success(request, "Registration Completed Successfully!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {"form": form})
