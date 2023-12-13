from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

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
    
    return render(request, 'home.html', {"records": records})

# def login_user(request):
#     ...

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            username = form.cleaned_data['username']

            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "You have successfully register")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def customer_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        return render(request, 'record.html', {"record":record})
    else:
        messages.success(request, "You must be logged in!!")
        return redirect('home')

def delete_record(request, id):
    if request.user.is_authenticated:
        delete_it =Record.objects.get(id=id)
        delete_it.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in!!")
        return redirect('home')
    
def add_record(request):
        form = AddRecordForm(request.POST or None)
        if request.user.is_authenticated:
            if request.method == 'POST':
                if form.is_valid():
                    add_record = form.save()
                    messages.success(request, "Record Added")
                    return redirect('home')
            return render(request, 'add_record.html', {'form':form})
        else:
            messages.success(request, "You must be logged in!!")
            return redirect('home')
        
def update_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in!!")
        return redirect('home')

        

