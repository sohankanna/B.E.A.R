from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import OrganizationSignUpForm
from .models import Organization
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Organization  # Assuming the model is named Organization
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Organization
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'simulator/home.html')

def about(request):
    return render(request, 'simulator/about.html')

def contact(request):
    return render(request, 'simulator/contact.html')



def signup(request):
    return render(request, 'simulator/signup.html')

def pricing(request):
    return render(request, 'simulator/pricing.html')

def signupsuccess(request):
    return render(request, 'simulator/signup_success.html')




def signup_view(request):
    if request.method == 'POST':
        org_name = request.POST.get('orgName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'simulator/signup.html')

        # Create the Organization object and save it to the database
        organization = Organization(org_name=org_name, email=email, phone=phone, password=password)
        organization.save()
        
        messages.success(request, "Organization created successfully")
        return redirect('signupsuccess')  # Redirect to the sign-in page or wherever appropriate
    
    return render(request, 'simulator/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = Organization.objects.get(email=email, password=password)  # You may want to use hashed passwords in production
            
            # Store the user's id in the session
            request.session['user_id'] = user.id
            
            return redirect('dashboard')  # Redirect to the dashboard view
        except Organization.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'simulator/login.html')

def dashboard_view(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        
        try:
            # Retrieve the specific organization based on the user_id
            user = Organization.objects.get(id=user_id)
            return render(request, 'simulator/dashboard.html', {'user': user})  # Pass the user object to the template
        except Organization.DoesNotExist:
            return redirect('login')  # Redirect if the user does not exist anymore
    else:
        return redirect('login')  # Redirect to login if not authenticated

def logout_view(request):
    request.session.flush()  # Clears the session
    return redirect('login')  # Redirect to login page after logout