from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.html')

def services(request):
    return HttpResponse("this is servicepage")

def login(request):
    return render(request, 'login.html')

def navbar(request):
    return render(request,'index.html')