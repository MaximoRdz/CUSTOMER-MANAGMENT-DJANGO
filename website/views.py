from django.shortcuts import render, redirect

# django authentication login system
from django.contrib.auth import authenticate, login, logout

# pop up messages
from django.contrib import messages

from .forms import SignUpForm

from .models import Record
from .forms import SignUpForm, AddRecordForm
# Create your views here.

def home(request):
    # page items: 
    records = Record.objects.all()
    # Check if logging in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']    
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Completed Successfully!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error While Logging In. \nPlease Try Again.")
            return redirect('home')
    else:       
        return render(request, 'home.html', {"records": records})


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
        # else:
        #     form = SignUpForm()
        #     return render(request, 'register.html', {"form": form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {"form": form})
    

def customer_record(request, pk):
    # pk: primary key
    # check if the user is authenticated
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {"customer_record": customer_record})
    else:
        messages.success(request, "You Must Be Logged In To Access Records")
        return redirect('home') 


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully")
        return redirect('home') 
    else:
        messages.success(request, "You Must Be Logged In To Manage Records")
        return redirect('home') 


def add_record(request):
    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":   
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home') 
        return render(request, 'add_record.html', {"form": form})
    else:
        messages.success(request, "You Must Be Logged In To Manage Records")
        return redirect('home') 

