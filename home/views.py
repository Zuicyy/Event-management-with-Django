from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, "Your message has been sent successfully!")

    return render(request,'contactus.html')

def login(request):
    return render(request, 'login.html')        


def thankyou(request):
    return render(request, 'thankyou.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if the passwords match
            if password != confirm_password:
                return render(request, 'registration/register.html', {'form': form, 'error_message': 'Passwords do not match.'})

            # Check if a user with the same username or email already exists
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return render(request, 'registration/register.html', {'form': form, 'error_message': 'Username or email already exists.'})

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)

            # Log the user in (optional)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            # Redirect to a success page or login page after successful registration
            return redirect('registration_success')

    else:
        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})
