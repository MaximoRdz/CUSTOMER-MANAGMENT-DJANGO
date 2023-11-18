from django.shortcuts import render, redirect

# django authentication login system
from django.contrib.auth import authenticate, login, logout

# pop up messages
from django.contrib import messages

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
    pass
