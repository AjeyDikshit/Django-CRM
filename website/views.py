from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # Check to see if logging in (Posting data)
    if request.method == "POST":
        # Do something
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
        else:
            messages.error(request, "There was an error logging in")
        return redirect('home')
    
    return render(request, 'home.html', {})

def login_user(request):
    ...

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!!")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
