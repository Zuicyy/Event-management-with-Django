from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
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

    return render(request,'contactus.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def thankyou(request):
    return render(request, 'thankyou.html')
