from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, HttpResponse
from home.models import Contact, UserProfile
from django.contrib import messages
from .forms import SignUpForm, LoginForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    user_profile = UserProfile.objects.filter(user_id=request.user.id).first()
    return render(request, 'index.html',{"user_profile": user_profile})

def about(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def profile(request):
    user_profile_form = UserProfileForm()
    if not request.user.is_authenticated:
        return redirect('login')

    user_profile = UserProfile.objects.filter(user_id=request.user.id).first()
    user = request.user
    if request.method == 'POST':
        if request.POST["first_name"]:
            user.first_name = request.POST["first_name"]
        if request.POST["last_name"]:
            user.last_name = request.POST["last_name"]
        o_password = request.POST["o_password"]
        n_password = request.POST["password"]
        if o_password and check_password(o_password, user.password):
            user.set_password(n_password)
            user.save()
        user.save()
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_profile_form.is_valid():
            user_profile_form.save()
            update_session_auth_hash(request, user)
        else:
            print(user_profile_form.errors)

    return render(request,'profile.html', {"user_profile_form":user_profile_form, "user":request.user,"up":user_profile})

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
        print(request.POST)
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
