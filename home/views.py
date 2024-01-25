from django.shortcuts import render, redirect, HttpResponse
from home.models import Contact
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated


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

#registration view
@user_not_authenticated
def register(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/')

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "New Account Created {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = SignUpForm()

    return render(
        request=request,
        template_name = "register.html",
        context={"form": form}
    )


#Login View
@user_not_authenticated
def login_user(request):
    # if request.user.is_authenticated:
    #     return redirect("home")

    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = LoginForm()

    return render(
        request=request,
        template_name="login.html",
        context={"form": form}
        )

#Logout View
@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')
