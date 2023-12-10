from django.shortcuts import render, HttpResponse

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
    
    return render(request,'contactus.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')