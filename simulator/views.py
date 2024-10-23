from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'simulator/home.html')

def about(request):
    return render(request, 'simulator/about.html')

def contact(request):
    return render(request, 'simulator/contact.html')

def login(request):
    return render(request, 'simulator/login.html')

def signup(request):
    return render(request, 'simulator/signup.html')